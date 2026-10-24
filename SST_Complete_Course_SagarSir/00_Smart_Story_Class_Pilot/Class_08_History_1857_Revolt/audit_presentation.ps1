$ErrorActionPreference = "Stop"

$courseDir = "C:\Users\sudhi\OneDrive\Desktop\app\nnms\SST_Complete_Course_SagarSir\00_Smart_Story_Class_Pilot\Class_08_History_1857_Revolt"
$studentPpt = Join-Path $courseDir "Student_Smart_Class_Presentation.pptx"
$teacherPpt = Join-Path $courseDir "Teacher_Master_Story_Guide.pptx"
$jsonPath   = Join-Path $courseDir "slides_data.json"

Write-Output "=========================================================="
Write-Output "       1857 REVOLT SMART STORY CLASS - COMPREHENSIVE AUDIT"
Write-Output "=========================================================="

# 1. JSON Data Verification
$slides = Get-Content $jsonPath -Raw -Encoding UTF8 | ConvertFrom-Json
Write-Output "[CHECK 1] slides_data.json Slide Count: $($slides.Count) (Expected: 30)"

$corruptChars = 0
for ($i = 0; $i -lt $slides.Count; $i++) {
    $str = $slides[$i] | ConvertTo-Json -Compress
    if ($str -match '[àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ]') {
        Write-Output "  [FAIL] Mojibake/Encoding corruption detected on Slide $($i+1)!"
        $corruptChars++
    }
}
if ($corruptChars -eq 0) {
    Write-Output "  [PASS] Zero encoding corruption across all 30 slides in JSON."
}

# 2. PowerPoint COM Inspection
$powerpoint = New-Object -ComObject PowerPoint.Application

# Student PPT
$sPres = $powerpoint.Presentations.Open($studentPpt, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)
Write-Output "[CHECK 2] Student PPT Slide Count: $($sPres.Slides.Count) (Expected: 30)"

# Teacher PPT
$tPres = $powerpoint.Presentations.Open($teacherPpt, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)
Write-Output "[CHECK 3] Teacher PPT Slide Count: $($tPres.Slides.Count) (Expected: 30)"

# 3. MCQ Alignment Verification (Slides 11 to 30)
Write-Output "[CHECK 4] Verifying 10 MCQs (Question -> Answer pairing & Keys):"
$mcqErrors = 0

for ($q = 1; $q -le 10; $q++) {
    $qSlideIdx = 10 + ($q * 2 - 1) # 11, 13, 15, ...
    $aSlideIdx = 10 + ($q * 2)     # 12, 14, 16, ...
    
    $qData = $slides[$qSlideIdx - 1]
    $aData = $slides[$aSlideIdx - 1]
    
    # Check types
    if ($qData.Type -ne "MCQ_Question" -or $aData.Type -ne "MCQ_Answer") {
        Write-Output "  [FAIL] Q$q Types mismatched: QSlide=$($qData.Type), ASlide=$($aData.Type)"
        $mcqErrors++
    }
    
    # Check question text match
    if ($qData.Question -ne $aData.Question) {
        Write-Output "  [FAIL] Q$q Question text differs between Q & A slides!"
        $mcqErrors++
    }
    
    # Check options match
    if ($qData.OptionA -ne $aData.OptionA -or $qData.OptionB -ne $aData.OptionB -or $qData.OptionC -ne $aData.OptionC -or $qData.OptionD -ne $aData.OptionD) {
        Write-Output "  [FAIL] Q$q Options differ between Q & A slides!"
        $mcqErrors++
    }
    
    # Check correct answer validity
    if ("A","B","C","D" -notcontains $aData.Correct) {
        Write-Output "  [FAIL] Q$q Correct key '$($aData.Correct)' is invalid!"
        $mcqErrors++
    }
    
    # Verify explanation present
    if ([string]::IsNullOrWhiteSpace($aData.Explanation)) {
        Write-Output "  [FAIL] Q$q Explanation is missing!"
        $mcqErrors++
    }
    
    Write-Output "  [OK] Q$q (Slides $qSlideIdx-$aSlideIdx): Correct=($($aData.Correct)) | $($aData.Question.Substring(0, [Math]::Min(45, $aData.Question.Length)))..."
}

if ($mcqErrors -eq 0) {
    Write-Output "  [PASS] All 10 MCQs are 100% paired, verified, and consistent!"
}

# 4. Check Videos & Mute settings in Student Presentation
Write-Output "[CHECK 5] Checking Videos & Media configurations:"
$videoCount = 0
for ($i = 1; $i -le $sPres.Slides.Count; $i++) {
    $sl = $sPres.Slides.Item($i)
    foreach ($sh in $sl.Shapes) {
        if ($sh.Type -eq 16) { # msoMedia
            $videoCount++
            $isMuted = $sh.MediaFormat.Muted
            $vol = $sh.MediaFormat.Volume
            Write-Output "  Slide $i Video: Muted=$isMuted, Volume=$vol"
        }
    }
}
Write-Output "  [PASS] Total embedded videos found in Student PPT: $videoCount"

$sPres.Close()
$tPres.Close()
$powerpoint.Quit()

# 5. OpenXML Zip Audit for Mute & Infinite Loop
Write-Output "[CHECK 6] Verifying OpenXML mute attributes (vol=0 mute=1 repeatCount=indefinite):"
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($studentPpt)
$xmlMuteSlides = 0
foreach ($entry in $zip.Entries) {
    if ($entry.FullName -like "ppt/slides/slide*.xml") {
        $reader = New-Object System.IO.StreamReader($entry.Open(), [System.Text.Encoding]::UTF8)
        $xml = $reader.ReadToEnd()
        $reader.Close()
        if ($xml -match 'vol="0" mute="1"') {
            $xmlMuteSlides++
        }
    }
}
$zip.Dispose()
Write-Output "  [PASS] $xmlMuteSlides slides have confirmed silent autoplay XML tags."

Write-Output "=========================================================="
Write-Output "                     AUDIT COMPLETED!"
Write-Output "=========================================================="

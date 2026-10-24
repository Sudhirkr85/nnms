$baseDir = "C:\Users\sudhi\OneDrive\Desktop\app\nnms\SST_Complete_Course_SagarSir\00_Smart_Story_Class_Pilot\Class_08_History_1857_Revolt"
$imgDir = "$baseDir\images"
$jsonPath = "$baseDir\slides_data.json"

function Get-RGB($r, $g, $b) {
    return [int]($r + ($g * 256) + ($b * 65536))
}

$cDarkBg    = Get-RGB 15 23 42      # Slate 900
$cCardBg    = Get-RGB 30 41 59      # Slate 800
$cGold      = Get-RGB 245 158 11    # Amber 500
$cGoldDark  = Get-RGB 180 83 9      # Amber 700
$cTextWhite = Get-RGB 248 250 252   # Slate 50
$cTextGray  = Get-RGB 203 213 225   # Slate 300
$cGreen     = Get-RGB 16 185 129    # Emerald 500
$cBlue      = Get-RGB 59 130 246    # Blue 500
$cBorder    = Get-RGB 51 65 85      # Slate 700

$rawJson = Get-Content -Path $jsonPath -Raw -Encoding UTF8
$slidesData = ConvertFrom-Json $rawJson

Write-Output "Loaded $($slidesData.Count) slides from JSON."
Write-Output "Starting PowerPoint COM engine..."
$ppt = New-Object -ComObject PowerPoint.Application

# ==============================================================
# BUILD PPT 1: STUDENT SMART CLASS PRESENTATION
# ==============================================================
Write-Output "`nCreating Student Smart Class Presentation with Auto-Playing Video..."
$presStudent = $ppt.Presentations.Add([Microsoft.Office.Core.MsoTriState]::msoFalse)
$presStudent.PageSetup.SlideWidth = 960
$presStudent.PageSetup.SlideHeight = 540

$slideNum = 0
foreach ($data in $slidesData) {
    $slideNum++
    Write-Output "  Building Student Slide $($slideNum): $($data.Title)"
    $slide = $presStudent.Slides.Add($presStudent.Slides.Count + 1, 12)
    
    # 1. Dark Background
    $slide.Background.Fill.Solid()
    $slide.Background.Fill.ForeColor.RGB = $cDarkBg
    
    # 2. Header Bar
    $hdr = $slide.Shapes.AddShape(1, 0, 0, 960, 48)
    $hdr.Fill.Solid()
    $hdr.Fill.ForeColor.RGB = $cCardBg
    $hdr.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
    
    # Title Text
    $tbTitle = $slide.Shapes.AddTextbox(1, 30, 6, 900, 36)
    $tbTitle.TextFrame.TextRange.Text = $data.Title
    $tbTitle.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbTitle.TextFrame.TextRange.Font.Size = 17
    $tbTitle.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbTitle.TextFrame.TextRange.Font.Color.RGB = $cGold
    
    # Top Shayari Pill (below header)
    $pill = $slide.Shapes.AddShape(5, 30, 56, 900, 34)
    $pill.Fill.Solid()
    $pill.Fill.ForeColor.RGB = Get-RGB 40 25 15
    $pill.Line.ForeColor.RGB = $cGoldDark
    $pill.Line.Weight = 1.5
    
    $tbShayari = $slide.Shapes.AddTextbox(1, 35, 58, 890, 30)
    $tbShayari.TextFrame.TextRange.Text = [string]($data.TopShayari)
    $tbShayari.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbShayari.TextFrame.TextRange.Font.Size = 12
    $tbShayari.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbShayari.TextFrame.TextRange.Font.Color.RGB = $cGold
    
    $fullImgPath = "$imgDir\$($data.ImgName)"
    $fullVidPath = if ($data.VideoName) { "$imgDir\$($data.VideoName)" } else { $null }
    
    if ($data.Type -eq "Title") {
        $card = $slide.Shapes.AddShape(5, 30, 98, 460, 395)
        $card.Fill.Solid()
        $card.Fill.ForeColor.RGB = $cCardBg
        $card.Line.ForeColor.RGB = $cBorder
        
        $tbSub = $slide.Shapes.AddTextbox(1, 45, 110, 430, 90)
        $tbSub.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbSub.TextFrame.TextRange.Text = $data.Subtitle
        $tbSub.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbSub.TextFrame.TextRange.Font.Size = 16
        $tbSub.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbSub.TextFrame.TextRange.Font.Color.RGB = $cTextWhite
        
        $tbB = $slide.Shapes.AddTextbox(1, 45, 210, 430, 160)
        $tbB.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbB.TextFrame.TextRange.Text = "$($data.Bullet1)`n`n$($data.Bullet2)`n`n$($data.Bullet3)"
        $tbB.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbB.TextFrame.TextRange.Font.Size = 13
        $tbB.TextFrame.TextRange.Font.Color.RGB = $cTextGray
        
        # Video on Right if available, else Image
        if ($fullVidPath -and (Test-Path $fullVidPath)) {
            $media = $slide.Shapes.AddMediaObject2($fullVidPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 505, 98, 425, 395)
            $media.AnimationSettings.PlaySettings.PlayOnEntry = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $media.AnimationSettings.PlaySettings.LoopUntilStopped = [Microsoft.Office.Core.MsoTriState]::msoTrue
        } elseif (Test-Path $fullImgPath) {
            $pic = $slide.Shapes.AddPicture($fullImgPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 505, 98, 425, 395)
        }
    }
    elseif ($data.Type -eq "Content") {
        # Video on Left if available, else Image
        if ($fullVidPath -and (Test-Path $fullVidPath)) {
            $media = $slide.Shapes.AddMediaObject2($fullVidPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 30, 98, 410, 395)
            $media.AnimationSettings.PlaySettings.PlayOnEntry = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $media.AnimationSettings.PlaySettings.LoopUntilStopped = [Microsoft.Office.Core.MsoTriState]::msoTrue
        } elseif (Test-Path $fullImgPath) {
            $pic = $slide.Shapes.AddPicture($fullImgPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 30, 98, 410, 395)
        }
        
        # Bullets Card on Right
        $card = $slide.Shapes.AddShape(5, 455, 98, 475, 280)
        $card.Fill.Solid()
        $card.Fill.ForeColor.RGB = $cCardBg
        $card.Line.ForeColor.RGB = $cBorder
        
        $tbContent = $slide.Shapes.AddTextbox(1, 470, 110, 445, 255)
        $tbContent.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbContent.TextFrame.TextRange.Text = "$($data.Bullet1)`n`n$($data.Bullet2)`n`n$($data.Bullet3)"
        $tbContent.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbContent.TextFrame.TextRange.Font.Size = 13.5
        $tbContent.TextFrame.TextRange.Font.Color.RGB = $cTextWhite
        
        # Exam Booster Box
        $eb = $slide.Shapes.AddShape(5, 455, 388, 475, 105)
        $eb.Fill.Solid()
        $eb.Fill.ForeColor.RGB = Get-RGB 20 40 30
        $eb.Line.ForeColor.RGB = $cGreen
        $eb.Line.Weight = 1.5
        
        $tbEb = $slide.Shapes.AddTextbox(1, 465, 396, 455, 85)
        $tbEb.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbEb.TextFrame.TextRange.Text = $data.ExamBooster
        $tbEb.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbEb.TextFrame.TextRange.Font.Size = 13
        $tbEb.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbEb.TextFrame.TextRange.Font.Color.RGB = Get-RGB 110 231 183
    }
    elseif ($data.Type -like "Quiz*") {
        $questions = @($data.Q1, $data.Q2, $data.Q3, $data.Q4, $data.Q5)
        $topY = 98
        foreach ($qText in $questions) {
            $qBox = $slide.Shapes.AddShape(5, 30, $topY, 900, 70)
            $qBox.Fill.Solid()
            $qBox.Fill.ForeColor.RGB = $cCardBg
            $qBox.Line.ForeColor.RGB = $cGoldDark
            
            $tbQ = $slide.Shapes.AddTextbox(1, 45, $topY + 12, 870, 50)
            $tbQ.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $tbQ.TextFrame.TextRange.Text = $qText
            $tbQ.TextFrame.TextRange.Font.Name = "Segoe UI"
            $tbQ.TextFrame.TextRange.Font.Size = 13.5
            $tbQ.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $tbQ.TextFrame.TextRange.Font.Color.RGB = $cTextWhite
            
            $topY += 78
        }
    }
    
    # Bottom Footer
    $ft = $slide.Shapes.AddTextbox(1, 30, 502, 900, 25)
    $ft.TextFrame.TextRange.Text = "Class 08: 1857 की महान क्रांति • NMMS All India SST Smart Class • सागर सर स्पेशल"
    $ft.TextFrame.TextRange.Font.Name = "Segoe UI"
    $ft.TextFrame.TextRange.Font.Size = 10
    $ft.TextFrame.TextRange.Font.Color.RGB = Get-RGB 100 116 139
}

$studentPptx = "$baseDir\Student_Smart_Class_Presentation.pptx"
$studentPdf  = "$baseDir\Student_Smart_Class_Presentation.pdf"
$presStudent.SaveAs($studentPptx)
$presStudent.SaveAs($studentPdf, 32)
$presStudent.Close()
Write-Output "Student Smart Class Presentation & PDF created successfully!"


# ==============================================================
# BUILD PPT 2: TEACHER MASTER STORY & SCRIPT GUIDE
# ==============================================================
Write-Output "`nCreating Teacher Master Story Guide Presentation..."
$presTeacher = $ppt.Presentations.Add([Microsoft.Office.Core.MsoTriState]::msoFalse)
$presTeacher.PageSetup.SlideWidth = 960
$presTeacher.PageSetup.SlideHeight = 540

$slideNum = 0
foreach ($data in $slidesData) {
    $slideNum++
    Write-Output "  Building Teacher Guide Slide $($slideNum): $($data.Title)"
    $slide = $presTeacher.Slides.Add($presTeacher.Slides.Count + 1, 12)
    
    $slide.Background.Fill.Solid()
    $slide.Background.Fill.ForeColor.RGB = Get-RGB 15 20 30
    
    $hdr = $slide.Shapes.AddShape(1, 0, 0, 960, 46)
    $hdr.Fill.Solid()
    $hdr.Fill.ForeColor.RGB = Get-RGB 30 35 50
    $hdr.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
    
    $tbTitle = $slide.Shapes.AddTextbox(1, 20, 6, 920, 34)
    $tbTitle.TextFrame.TextRange.Text = "शिक्षक मास्टर गाइड [स्लाइड $slideNum]: " + $data.Title
    $tbTitle.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbTitle.TextFrame.TextRange.Font.Size = 15
    $tbTitle.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbTitle.TextFrame.TextRange.Font.Color.RGB = $cGold
    
    $fullImgPath = "$imgDir\$($data.ImgName)"
    $fullVidPath = if ($data.VideoName) { "$imgDir\$($data.VideoName)" } else { $null }
    
    # Left Column: Screen Snapshot / Video
    $leftBox = $slide.Shapes.AddShape(5, 20, 54, 360, 470)
    $leftBox.Fill.Solid()
    $leftBox.Fill.ForeColor.RGB = Get-RGB 24 29 45
    $leftBox.Line.ForeColor.RGB = $cBorder
    
    $tbLeftHdr = $slide.Shapes.AddTextbox(1, 28, 60, 340, 26)
    $tbLeftHdr.TextFrame.TextRange.Text = "स्क्रीन पर छात्र क्या देख रहे हैं:"
    $tbLeftHdr.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbLeftHdr.TextFrame.TextRange.Font.Size = 12
    $tbLeftHdr.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbLeftHdr.TextFrame.TextRange.Font.Color.RGB = $cGold
    
    if ($fullVidPath -and (Test-Path $fullVidPath)) {
        $media = $slide.Shapes.AddMediaObject2($fullVidPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 30, 90, 340, 195)
        $media.AnimationSettings.PlaySettings.PlayOnEntry = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $media.AnimationSettings.PlaySettings.LoopUntilStopped = [Microsoft.Office.Core.MsoTriState]::msoTrue
    } elseif (Test-Path $fullImgPath) {
        $pic = $slide.Shapes.AddPicture($fullImgPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 30, 90, 340, 195)
    }
    
    $tbLeftTxt = $slide.Shapes.AddTextbox(1, 28, 295, 344, 220)
    $tbLeftTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    if ($data.Type -like "Quiz*") {
        $tbLeftTxt.TextFrame.TextRange.Text = "टेस्ट प्रश्न:`n$($data.Q1)`n`n$($data.Q2)`n`n$($data.Q3)"
    } else {
        $tbLeftTxt.TextFrame.TextRange.Text = "मुख्य बिंदु:`n$($data.Bullet1)`n`n$($data.Bullet2)`n`n$($data.ExamBooster)"
    }
    $tbLeftTxt.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbLeftTxt.TextFrame.TextRange.Font.Size = 10.5
    $tbLeftTxt.TextFrame.TextRange.Font.Color.RGB = $cTextGray
    
    # Right Column Top: Teacher's Speaking Script
    $scriptBox = $slide.Shapes.AddShape(5, 395, 54, 545, 260)
    $scriptBox.Fill.Solid()
    $scriptBox.Fill.ForeColor.RGB = Get-RGB 20 35 25
    $scriptBox.Line.ForeColor.RGB = $cGreen
    $scriptBox.Line.Weight = 1.5
    
    $tbScrHdr = $slide.Shapes.AddTextbox(1, 405, 58, 525, 24)
    $tbScrHdr.TextFrame.TextRange.Text = "शिक्षक के लिए कथावाचक डायलॉग (Teacher Script):"
    $tbScrHdr.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbScrHdr.TextFrame.TextRange.Font.Size = 12
    $tbScrHdr.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbScrHdr.TextFrame.TextRange.Font.Color.RGB = Get-RGB 110 231 183
    
    $tbScrTxt = $slide.Shapes.AddTextbox(1, 405, 84, 525, 225)
    $tbScrTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbScrTxt.TextFrame.TextRange.Text = $data.TeacherScript
    $tbScrTxt.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbScrTxt.TextFrame.TextRange.Font.Size = 11.5
    $tbScrTxt.TextFrame.TextRange.Font.Color.RGB = $cTextWhite
    
    # Right Column Middle: Desi Punch & Humor
    $punchBox = $slide.Shapes.AddShape(5, 395, 320, 545, 92)
    $punchBox.Fill.Solid()
    $punchBox.Fill.ForeColor.RGB = Get-RGB 45 25 15
    $punchBox.Line.ForeColor.RGB = $cGold
    
    $tbPnHdr = $slide.Shapes.AddTextbox(1, 405, 324, 525, 22)
    $tbPnHdr.TextFrame.TextRange.Text = "देसी पंच, हास्य व शायरी (Funny Punchline):"
    $tbPnHdr.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbPnHdr.TextFrame.TextRange.Font.Size = 11
    $tbPnHdr.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbPnHdr.TextFrame.TextRange.Font.Color.RGB = $cGold
    
    $tbPnTxt = $slide.Shapes.AddTextbox(1, 405, 344, 525, 62)
    $tbPnTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbPnTxt.TextFrame.TextRange.Text = "$($data.TeacherPunch)`nशायरी: $($data.TopShayari)"
    $tbPnTxt.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbPnTxt.TextFrame.TextRange.Font.Size = 10.5
    $tbPnTxt.TextFrame.TextRange.Font.Color.RGB = Get-RGB 254 243 199
    
    # Right Column Bottom: AI 3D Prompt
    $aiBox = $slide.Shapes.AddShape(5, 395, 418, 545, 106)
    $aiBox.Fill.Solid()
    $aiBox.Fill.ForeColor.RGB = Get-RGB 20 25 40
    $aiBox.Line.ForeColor.RGB = $cBlue
    
    $tbAiHdr = $slide.Shapes.AddTextbox(1, 405, 422, 525, 22)
    $tbAiHdr.TextFrame.TextRange.Text = "AI 3D Image & Video Prompt (Google Vids / Kling / Runway):"
    $tbAiHdr.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbAiHdr.TextFrame.TextRange.Font.Size = 10.5
    $tbAiHdr.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbAiHdr.TextFrame.TextRange.Font.Color.RGB = Get-RGB 147 197 253
    
    $tbAiTxt = $slide.Shapes.AddTextbox(1, 405, 442, 525, 78)
    $tbAiTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbAiTxt.TextFrame.TextRange.Text = $data.AIPrompt
    $tbAiTxt.TextFrame.TextRange.Font.Name = "Consolas"
    $tbAiTxt.TextFrame.TextRange.Font.Size = 9.5
    $tbAiTxt.TextFrame.TextRange.Font.Color.RGB = Get-RGB 226 232 240
}

$teacherPptx = "$baseDir\Teacher_Master_Story_Guide.pptx"
$teacherPdf  = "$baseDir\Teacher_Master_Story_Guide.pdf"
$presTeacher.SaveAs($teacherPptx)
$presTeacher.SaveAs($teacherPdf, 32)
$presTeacher.Close()
Write-Output "Teacher Master Story Guide Presentation & PDF created successfully!"

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
Write-Output "`nAll tasks finished! Both PPTX and PDF editions are ready in:`n$baseDir"

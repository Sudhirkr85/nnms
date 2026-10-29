$baseDir = "C:\Users\sudhi\OneDrive\Desktop\New folder\nnms\SST_Complete_Course_SagarSir\00_Smart_Story_Class_Pilot\Class_08_History_1857_Revolt"
$imgDir = if (Test-Path "$baseDir\images") { "$baseDir\images" } else { "C:\Users\sudhi\.gemini\antigravity\brain\13b57667-ad5e-4cda-811d-01ef90f919b6\scratch\images_backup" }
$jsonPath = "$baseDir\slides_data.json"
$labelsPath = "$baseDir\ui_labels.json"

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

$labels = Get-Content -Path $labelsPath -Raw -Encoding UTF8 | ConvertFrom-Json

Write-Output "Loaded $($slidesData.Count) slides."
Write-Output "Starting PowerPoint COM engine..."
$ppt = New-Object -ComObject PowerPoint.Application

# ==============================================================
# BUILD PPT 1: STUDENT SMART CLASS PRESENTATION
# ==============================================================
Write-Output "`nCreating Student Smart Class Presentation..."
$presStudent = $ppt.Presentations.Add([Microsoft.Office.Core.MsoTriState]::msoFalse)
$presStudent.PageSetup.SlideWidth = 960
$presStudent.PageSetup.SlideHeight = 540

$slideNum = 0
foreach ($data in $slidesData) {
    $slideNum++
    Write-Output "  Building Student Slide $($slideNum): $($data.Title)"
    $slide = $presStudent.Slides.Add($presStudent.Slides.Count + 1, 12)
    
    $slide.Background.Fill.Solid()
    $slide.Background.Fill.ForeColor.RGB = $cDarkBg
    
    $fullImgPath = "$imgDir\$($data.ImgName)"
    $fullVidPath = if ($data.VideoName) { "$imgDir\$($data.VideoName)" } else { $null }
    
    if ($data.Type -eq "Branding") {
        # 1. Outer Deep Royal Navy Card
        $card = $slide.Shapes.AddShape(5, 36, 24, 888, 492)
        $card.Fill.Solid()
        $card.Fill.ForeColor.RGB = Get-RGB 30 58 138     # #1E3A8A (Navy Blue)
        $card.Line.ForeColor.RGB = Get-RGB 217 119 6    # #D97706 (Amber Gold)
        $card.Line.Weight = 3
        
        # 2. Centered Official Circular Logo (Width 130, Height 130, Centered at X=415)
        if (Test-Path $fullImgPath) {
            $pic = $slide.Shapes.AddPicture($fullImgPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 415, 46, 130, 130)
        }
        
        # 3. Institute Name
        $tbBrand = $slide.Shapes.AddTextbox(1, 60, 192, 840, 36)
        $tbBrand.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbBrand.TextFrame.TextRange.Text = [string]$data.Title
        $tbBrand.TextFrame.TextRange.ParagraphFormat.Alignment = 2 # Center
        $tbBrand.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbBrand.TextFrame.TextRange.Font.Size = 24
        $tbBrand.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbBrand.TextFrame.TextRange.Font.Color.RGB = Get-RGB 253 230 138 # Light Gold
        
        # 4. Exam & Class Details
        $tbSub = $slide.Shapes.AddTextbox(1, 60, 234, 840, 28)
        $tbSub.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbSub.TextFrame.TextRange.Text = [string]$data.Subtitle
        $tbSub.TextFrame.TextRange.ParagraphFormat.Alignment = 2 # Center
        $tbSub.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbSub.TextFrame.TextRange.Font.Size = 15
        $tbSub.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbSub.TextFrame.TextRange.Font.Color.RGB = Get-RGB 147 197 253 # Sky Blue
        
        # 5. Main Topic (1857 की महान क्रांति)
        $tbTopic = $slide.Shapes.AddTextbox(1, 60, 288, 840, 56)
        $tbTopic.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbTopic.TextFrame.TextRange.Text = [string]$data.TopicHindi
        $tbTopic.TextFrame.TextRange.ParagraphFormat.Alignment = 2 # Center
        $tbTopic.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbTopic.TextFrame.TextRange.Font.Size = 38
        $tbTopic.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbTopic.TextFrame.TextRange.Font.Color.RGB = Get-RGB 255 255 255 # White
        
        # 6. English Subtopic
        $tbTopicEn = $slide.Shapes.AddTextbox(1, 60, 350, 840, 32)
        $tbTopicEn.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbTopicEn.TextFrame.TextRange.Text = [string]$data.TopicEnglish
        $tbTopicEn.TextFrame.TextRange.ParagraphFormat.Alignment = 2 # Center
        $tbTopicEn.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbTopicEn.TextFrame.TextRange.Font.Size = 16
        $tbTopicEn.TextFrame.TextRange.Font.Color.RGB = Get-RGB 241 245 249 # Slate 100
        
        # 7. Our Details Badge Card
        $badgeCard = $slide.Shapes.AddShape(5, 230, 412, 500, 56)
        $badgeCard.Fill.Solid()
        $badgeCard.Fill.ForeColor.RGB = Get-RGB 6 78 59 # Dark Emerald Green
        $badgeCard.Line.ForeColor.RGB = Get-RGB 217 119 6 # Amber Gold
        $badgeCard.Line.Weight = 1.5
        
        $tbBadge = $slide.Shapes.AddTextbox(1, 235, 422, 490, 36)
        $tbBadge.TextFrame.TextRange.Text = [string]$data.Faculty + "  |  sagarcoaching.tech"
        $tbBadge.TextFrame.TextRange.ParagraphFormat.Alignment = 2 # Center
        $tbBadge.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbBadge.TextFrame.TextRange.Font.Size = 14
        $tbBadge.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbBadge.TextFrame.TextRange.Font.Color.RGB = Get-RGB 253 230 138 # Light Gold
    }
    elseif ($data.Type -eq "MCQ_Question") {
        # Header Bar
        $hdr = $slide.Shapes.AddShape(1, 0, 0, 960, 48)
        $hdr.Fill.Solid()
        $hdr.Fill.ForeColor.RGB = $cCardBg
        $hdr.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
        
        $tbTitle = $slide.Shapes.AddTextbox(1, 30, 6, 900, 36)
        $tbTitle.TextFrame.TextRange.Text = [string]$data.Title
        $tbTitle.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbTitle.TextFrame.TextRange.Font.Size = 16
        $tbTitle.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbTitle.TextFrame.TextRange.Font.Color.RGB = $cGold
        
        # Question Box
        $qBox = $slide.Shapes.AddShape(5, 36, 62, 888, 105)
        $qBox.Fill.Solid()
        $qBox.Fill.ForeColor.RGB = Get-RGB 30 58 138 # Deep Navy #1E3A8A
        $qBox.Line.ForeColor.RGB = Get-RGB 217 119 6 # Amber Gold
        $qBox.Line.Weight = 2
        
        $tbQ = $slide.Shapes.AddTextbox(1, 50, 68, 860, 92)
        $tbQ.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbQ.TextFrame.TextRange.Text = [string]$data.Question
        $tbQ.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbQ.TextFrame.TextRange.Font.Size = 16.5
        $tbQ.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbQ.TextFrame.TextRange.Font.Color.RGB = Get-RGB 255 255 255
        
        # 4 Options Grid (2x2)
        $optPositions = @(
            @{ X = 36;  Y = 182; Text = $data.OptionA; Key = "A" },
            @{ X = 494; Y = 182; Text = $data.OptionB; Key = "B" },
            @{ X = 36;  Y = 278; Text = $data.OptionC; Key = "C" },
            @{ X = 494; Y = 278; Text = $data.OptionD; Key = "D" }
        )
        
        foreach ($opt in $optPositions) {
            $optBox = $slide.Shapes.AddShape(5, $opt.X, $opt.Y, 430, 80)
            $optBox.Fill.Solid()
            $optBox.Fill.ForeColor.RGB = $cCardBg
            $optBox.Line.ForeColor.RGB = Get-RGB 71 85 105
            $optBox.Line.Weight = 1.5
            
            $tbOpt = $slide.Shapes.AddTextbox(1, $opt.X + 15, $opt.Y + 12, 400, 56)
            $tbOpt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $tbOpt.TextFrame.TextRange.Text = [string]$opt.Text
            $tbOpt.TextFrame.TextRange.Font.Name = "Segoe UI"
            $tbOpt.TextFrame.TextRange.Font.Size = 15.5
            $tbOpt.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $tbOpt.TextFrame.TextRange.Font.Color.RGB = Get-RGB 248 250 252
        }
        
        # Timer / Thinking Pill
        $pill = $slide.Shapes.AddShape(5, 230, 380, 500, 56)
        $pill.Fill.Solid()
        $pill.Fill.ForeColor.RGB = Get-RGB 49 46 129
        $pill.Line.ForeColor.RGB = Get-RGB 99 102 241
        $pill.Line.Weight = 1.5
        
        $tbPill = $slide.Shapes.AddTextbox(1, 235, 388, 490, 40)
        $tbPill.TextFrame.TextRange.Text = [char]::ConvertFromUtf32(0x23F1) + " " + [string]$labels.TimerHint
        $tbPill.TextFrame.TextRange.ParagraphFormat.Alignment = 2 # Center
        $tbPill.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbPill.TextFrame.TextRange.Font.Size = 14
        $tbPill.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbPill.TextFrame.TextRange.Font.Color.RGB = Get-RGB 253 230 138
        
        # Bottom Footer
        $ft = $slide.Shapes.AddTextbox(1, 30, 502, 900, 25)
        $ft.TextFrame.TextRange.Text = [string]$labels.StudentFooter
        $ft.TextFrame.TextRange.Font.Name = "Segoe UI"
        $ft.TextFrame.TextRange.Font.Size = 10
        $ft.TextFrame.TextRange.Font.Color.RGB = Get-RGB 100 116 139
    }
    elseif ($data.Type -eq "MCQ_Answer") {
        # Header Bar
        $hdr = $slide.Shapes.AddShape(1, 0, 0, 960, 48)
        $hdr.Fill.Solid()
        $hdr.Fill.ForeColor.RGB = $cCardBg
        $hdr.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
        
        $tbTitle = $slide.Shapes.AddTextbox(1, 30, 6, 900, 36)
        $tbTitle.TextFrame.TextRange.Text = [string]$data.Title
        $tbTitle.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbTitle.TextFrame.TextRange.Font.Size = 16
        $tbTitle.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbTitle.TextFrame.TextRange.Font.Color.RGB = $cGreen
        
        # Question Box
        $qBox = $slide.Shapes.AddShape(5, 36, 62, 888, 105)
        $qBox.Fill.Solid()
        $qBox.Fill.ForeColor.RGB = Get-RGB 30 58 138
        $qBox.Line.ForeColor.RGB = Get-RGB 217 119 6
        $qBox.Line.Weight = 2
        
        $tbQ = $slide.Shapes.AddTextbox(1, 50, 68, 860, 92)
        $tbQ.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbQ.TextFrame.TextRange.Text = [string]$data.Question
        $tbQ.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbQ.TextFrame.TextRange.Font.Size = 16.5
        $tbQ.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbQ.TextFrame.TextRange.Font.Color.RGB = Get-RGB 255 255 255
        
        # 4 Options Grid (2x2) with Correct Answer Highlighted in Bright Green!
        $optPositions = @(
            @{ X = 36;  Y = 182; Text = $data.OptionA; Key = "A" },
            @{ X = 494; Y = 182; Text = $data.OptionB; Key = "B" },
            @{ X = 36;  Y = 278; Text = $data.OptionC; Key = "C" },
            @{ X = 494; Y = 278; Text = $data.OptionD; Key = "D" }
        )
        
        foreach ($opt in $optPositions) {
            $isCorrect = ($opt.Key -eq $data.Correct)
            
            $optBox = $slide.Shapes.AddShape(5, $opt.X, $opt.Y, 430, 80)
            $optBox.Fill.Solid()
            
            if ($isCorrect) {
                $optBox.Fill.ForeColor.RGB = Get-RGB 20 83 45 # Green 900
                $optBox.Line.ForeColor.RGB = Get-RGB 34 197 94 # Emerald 500
                $optBox.Line.Weight = 2.5
            } else {
                $optBox.Fill.ForeColor.RGB = Get-RGB 15 23 42 # Slate 900
                $optBox.Line.ForeColor.RGB = Get-RGB 51 65 85 # Slate 700
                $optBox.Line.Weight = 1
            }
            
            $tbOpt = $slide.Shapes.AddTextbox(1, $opt.X + 15, $opt.Y + 12, 400, 56)
            $tbOpt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $tbOpt.TextFrame.TextRange.Font.Name = "Segoe UI"
            if ($isCorrect) {
                $tbOpt.TextFrame.TextRange.Text = [char]::ConvertFromUtf32(0x2705) + "  " + [string]$opt.Text
                $tbOpt.TextFrame.TextRange.Font.Size = 16
                $tbOpt.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
                $tbOpt.TextFrame.TextRange.Font.Color.RGB = Get-RGB 253 230 138
            } else {
                $tbOpt.TextFrame.TextRange.Text = [string]$opt.Text
                $tbOpt.TextFrame.TextRange.Font.Size = 14
                $tbOpt.TextFrame.TextRange.Font.Color.RGB = Get-RGB 148 163 184
            }
        }
        
        # Bottom Explanation Banner
        $expBox = $slide.Shapes.AddShape(5, 36, 372, 888, 112)
        $expBox.Fill.Solid()
        $expBox.Fill.ForeColor.RGB = Get-RGB 6 78 59
        $expBox.Line.ForeColor.RGB = Get-RGB 16 185 129
        $expBox.Line.Weight = 2
        
        $tbExpHdr = $slide.Shapes.AddTextbox(1, 50, 376, 860, 26)
        $tbExpHdr.TextFrame.TextRange.Text = [char]::ConvertFromUtf32(0x2705) + " " + ($labels.AnswerBanner -f [string]$data.Correct)
        $tbExpHdr.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbExpHdr.TextFrame.TextRange.Font.Size = 14
        $tbExpHdr.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbExpHdr.TextFrame.TextRange.Font.Color.RGB = Get-RGB 253 230 138
        
        $tbExpTxt = $slide.Shapes.AddTextbox(1, 50, 402, 860, 76)
        $tbExpTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbExpTxt.TextFrame.TextRange.Text = [char]::ConvertFromUtf32(0x1F4A1) + "  " + [string]$data.Explanation
        $tbExpTxt.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbExpTxt.TextFrame.TextRange.Font.Size = 13.5
        $tbExpTxt.TextFrame.TextRange.Font.Color.RGB = Get-RGB 255 255 255
        
        # Bottom Footer
        $ft = $slide.Shapes.AddTextbox(1, 30, 502, 900, 25)
        $ft.TextFrame.TextRange.Text = [string]$labels.StudentFooter
        $ft.TextFrame.TextRange.Font.Name = "Segoe UI"
        $ft.TextFrame.TextRange.Font.Size = 10
        $ft.TextFrame.TextRange.Font.Color.RGB = Get-RGB 100 116 139
    }
    else {
        # Regular Story Slides (Scenes 1 to 9)
        $hdr = $slide.Shapes.AddShape(1, 0, 0, 960, 48)
        $hdr.Fill.Solid()
        $hdr.Fill.ForeColor.RGB = $cCardBg
        $hdr.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
        
        $tbTitle = $slide.Shapes.AddTextbox(1, 30, 6, 900, 36)
        $tbTitle.TextFrame.TextRange.Text = [string]$data.Title
        $tbTitle.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbTitle.TextFrame.TextRange.Font.Size = 16
        $tbTitle.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbTitle.TextFrame.TextRange.Font.Color.RGB = $cGold
        
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
        
        if ($fullVidPath -and (Test-Path $fullVidPath)) {
            $media = $slide.Shapes.AddMediaObject2($fullVidPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 30, 98, 410, 395)
            
            # Mute Audio Completely
            $media.MediaFormat.Muted = $true
            $media.MediaFormat.Volume = 0.0
            
            # Infinite Loop and Autoplay Settings
            $media.AnimationSettings.PlaySettings.PlayOnEntry = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $media.AnimationSettings.PlaySettings.LoopUntilStopped = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $media.AnimationSettings.PlaySettings.RewindMovie = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $media.AnimationSettings.PlaySettings.HideWhileNotPlaying = [Microsoft.Office.Core.MsoTriState]::msoFalse
            $media.AnimationSettings.PlaySettings.PauseAnimation = [Microsoft.Office.Core.MsoTriState]::msoFalse
            
            for ($k = 1; $k -le $slide.TimeLine.MainSequence.Count; $k++) {
                $eff = $slide.TimeLine.MainSequence.Item($k)
                if ($eff.Shape.Id -eq $media.Id) {
                    $eff.Timing.TriggerType = 2 # msoAnimTriggerWithPrevious
                    $eff.Timing.TriggerDelayTime = 0
                    $eff.Timing.RepeatCount = 1000
                }
            }
        } elseif (Test-Path $fullImgPath) {
            $pic = $slide.Shapes.AddPicture($fullImgPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 30, 98, 410, 395)
        }
        
        $card = $slide.Shapes.AddShape(5, 455, 98, 475, 280)
        $card.Fill.Solid()
        $card.Fill.ForeColor.RGB = $cCardBg
        $card.Line.ForeColor.RGB = $cBorder
        
        $tbContent = $slide.Shapes.AddTextbox(1, 470, 108, 445, 260)
        $tbContent.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbContent.TextFrame.TextRange.Text = "$($data.Bullet1)`n`n$($data.Bullet2)`n`n$($data.Bullet3)"
        $tbContent.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbContent.TextFrame.TextRange.Font.Size = 13
        $tbContent.TextFrame.TextRange.Font.Color.RGB = $cTextWhite
        
        $eb = $slide.Shapes.AddShape(5, 455, 388, 475, 105)
        $eb.Fill.Solid()
        $eb.Fill.ForeColor.RGB = Get-RGB 20 40 30
        $eb.Line.ForeColor.RGB = $cGreen
        $eb.Line.Weight = 1.5
        
        $tbEb = $slide.Shapes.AddTextbox(1, 465, 396, 455, 85)
        $tbEb.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbEb.TextFrame.TextRange.Text = [string]$data.ExamBooster
        $tbEb.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbEb.TextFrame.TextRange.Font.Size = 12.5
        $tbEb.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbEb.TextFrame.TextRange.Font.Color.RGB = Get-RGB 110 231 183
        
        # Bottom Footer on Regular Slides
        $ft = $slide.Shapes.AddTextbox(1, 30, 502, 900, 25)
        $ft.TextFrame.TextRange.Text = [string]$labels.StudentFooter
        $ft.TextFrame.TextRange.Font.Name = "Segoe UI"
        $ft.TextFrame.TextRange.Font.Size = 10
        $ft.TextFrame.TextRange.Font.Color.RGB = Get-RGB 100 116 139
    }
}

$studentPptx = "$baseDir\Student_Smart_Class_Presentation.pptx"
$studentPdf  = "$baseDir\Student_Smart_Class_Presentation.pdf"
Remove-Item $studentPptx, $studentPdf -Force -ErrorAction SilentlyContinue
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
    $tbTitle.TextFrame.TextRange.Text = ($labels.TeacherGuideHeader -f $slideNum, [string]$data.Title)
    $tbTitle.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbTitle.TextFrame.TextRange.Font.Size = 14
    $tbTitle.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbTitle.TextFrame.TextRange.Font.Color.RGB = $cGold
    
    $fullImgPath = "$imgDir\$($data.ImgName)"
    $fullVidPath = if ($data.VideoName) { "$imgDir\$($data.VideoName)" } else { $null }
    
    # Left Column: Screen Snapshot
    $leftBox = $slide.Shapes.AddShape(5, 20, 54, 360, 470)
    $leftBox.Fill.Solid()
    $leftBox.Fill.ForeColor.RGB = Get-RGB 24 29 45
    $leftBox.Line.ForeColor.RGB = $cBorder
    
    $tbLeftHdr = $slide.Shapes.AddTextbox(1, 28, 60, 340, 26)
    $tbLeftHdr.TextFrame.TextRange.Text = [string]$labels.ScreenViewHeader
    $tbLeftHdr.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbLeftHdr.TextFrame.TextRange.Font.Size = 12
    $tbLeftHdr.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbLeftHdr.TextFrame.TextRange.Font.Color.RGB = $cGold
    
    if ($data.Type -eq "Branding") {
        if (Test-Path $fullImgPath) {
            $pic = $slide.Shapes.AddPicture($fullImgPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 135, 95, 130, 130)
        }
        
        $tbLeftTxt = $slide.Shapes.AddTextbox(1, 28, 235, 344, 275)
        $tbLeftTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbLeftTxt.TextFrame.TextRange.Text = "$($labels.BrandingDetails)`n`n* $($data.Title)`n* $($data.Subtitle)`n* $($data.TopicHindi)`n* $($data.Faculty)`n* $($data.Footer)"
        $tbLeftTxt.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbLeftTxt.TextFrame.TextRange.Font.Size = 10
        $tbLeftTxt.TextFrame.TextRange.Font.Color.RGB = $cTextGray
    }
    elseif ($data.Type -like "MCQ*") {
        $tbLeftTxt = $slide.Shapes.AddTextbox(1, 28, 90, 344, 420)
        $tbLeftTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        if ($data.Type -eq "MCQ_Question") {
            $tbLeftTxt.TextFrame.TextRange.Text = "प्रश्न:`n$($data.Question)`n`nविकल्प:`n$($data.OptionA)`n$($data.OptionB)`n$($data.OptionC)`n$($data.OptionD)`n`n[छात्र उत्तर सोच रहे हैं...]"
        } else {
            $tbLeftTxt.TextFrame.TextRange.Text = "प्रश्न:`n$($data.Question)`n`nसही उत्तर: ($($data.Correct))`n`nव्याख्या:`n$($data.Explanation)"
        }
        $tbLeftTxt.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbLeftTxt.TextFrame.TextRange.Font.Size = 10.5
        $tbLeftTxt.TextFrame.TextRange.Font.Color.RGB = $cTextWhite
    }
    else {
        if ($fullVidPath -and (Test-Path $fullVidPath)) {
            $media = $slide.Shapes.AddMediaObject2($fullVidPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 30, 90, 340, 195)
            $media.MediaFormat.Muted = $true
            $media.MediaFormat.Volume = 0.0
            $media.AnimationSettings.PlaySettings.PlayOnEntry = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $media.AnimationSettings.PlaySettings.LoopUntilStopped = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $media.AnimationSettings.PlaySettings.RewindMovie = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $media.AnimationSettings.PlaySettings.HideWhileNotPlaying = [Microsoft.Office.Core.MsoTriState]::msoFalse
            $media.AnimationSettings.PlaySettings.PauseAnimation = [Microsoft.Office.Core.MsoTriState]::msoFalse
            
            for ($k = 1; $k -le $slide.TimeLine.MainSequence.Count; $k++) {
                $eff = $slide.TimeLine.MainSequence.Item($k)
                if ($eff.Shape.Id -eq $media.Id) {
                    $eff.Timing.TriggerType = 2
                    $eff.Timing.TriggerDelayTime = 0
                    $eff.Timing.RepeatCount = 1000
                }
            }
        } elseif (Test-Path $fullImgPath) {
            $pic = $slide.Shapes.AddPicture($fullImgPath, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 30, 90, 340, 195)
        }
        
        $tbLeftTxt = $slide.Shapes.AddTextbox(1, 28, 295, 344, 220)
        $tbLeftTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $tbLeftTxt.TextFrame.TextRange.Text = "$($labels.KeyExamPoints)`n$($data.Bullet1)`n`n$($data.Bullet2)`n`n$($data.ExamBooster)"
        $tbLeftTxt.TextFrame.TextRange.Font.Name = "Segoe UI"
        $tbLeftTxt.TextFrame.TextRange.Font.Size = 10
        $tbLeftTxt.TextFrame.TextRange.Font.Color.RGB = $cTextGray
    }
    
    # Right Column Top: Teacher's Speaking Script
    $scriptBox = $slide.Shapes.AddShape(5, 395, 54, 545, 260)
    $scriptBox.Fill.Solid()
    $scriptBox.Fill.ForeColor.RGB = Get-RGB 20 35 25
    $scriptBox.Line.ForeColor.RGB = $cGreen
    $scriptBox.Line.Weight = 1.5
    
    $tbScrHdr = $slide.Shapes.AddTextbox(1, 405, 58, 525, 24)
    $tbScrHdr.TextFrame.TextRange.Text = [string]$labels.TeacherDialogueHeader
    $tbScrHdr.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbScrHdr.TextFrame.TextRange.Font.Size = 12
    $tbScrHdr.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbScrHdr.TextFrame.TextRange.Font.Color.RGB = Get-RGB 110 231 183
    
    $tbScrTxt = $slide.Shapes.AddTextbox(1, 405, 84, 525, 225)
    $tbScrTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    if ($data.Type -eq "MCQ_Question") {
        $tbScrTxt.TextFrame.TextRange.Text = "$($labels.TeacherQuestionPrompt)`n`n$($data.Question)`n`n10, 9, 8, 7, 6, 5, 4, 3, 2, 1..."
    } elseif ($data.Type -eq "MCQ_Answer") {
        $tbScrTxt.TextFrame.TextRange.Text = "$($labels.TeacherAnswerPrompt -f $data.Correct)`n`n$($data.Explanation)"
    } else {
        $tbScrTxt.TextFrame.TextRange.Text = [string]$data.TeacherScript
    }
    $tbScrTxt.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbScrTxt.TextFrame.TextRange.Font.Size = 11
    $tbScrTxt.TextFrame.TextRange.Font.Color.RGB = $cTextWhite
    
    # Right Column Middle: Desi Punch & Humor
    $punchBox = $slide.Shapes.AddShape(5, 395, 320, 545, 92)
    $punchBox.Fill.Solid()
    $punchBox.Fill.ForeColor.RGB = Get-RGB 45 25 15
    $punchBox.Line.ForeColor.RGB = $cGold
    
    $tbPnHdr = $slide.Shapes.AddTextbox(1, 405, 324, 525, 22)
    $tbPnHdr.TextFrame.TextRange.Text = [string]$labels.PunchHeader
    $tbPnHdr.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbPnHdr.TextFrame.TextRange.Font.Size = 11
    $tbPnHdr.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbPnHdr.TextFrame.TextRange.Font.Color.RGB = $cGold
    
    $tbPnTxt = $slide.Shapes.AddTextbox(1, 405, 344, 525, 62)
    $tbPnTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    if ($data.Type -eq "MCQ_Question") {
        $tbPnTxt.TextFrame.TextRange.Text = "$($labels.TeacherChallenge)"
    } elseif ($data.Type -eq "MCQ_Answer") {
        $tbPnTxt.TextFrame.TextRange.Text = "$($labels.TeacherSuccess)"
    } else {
        $tbPnTxt.TextFrame.TextRange.Text = "$($data.TeacherPunch)`n$($labels.ShayariPrefix) $($data.TopShayari)"
    }
    $tbPnTxt.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbPnTxt.TextFrame.TextRange.Font.Size = 10
    $tbPnTxt.TextFrame.TextRange.Font.Color.RGB = Get-RGB 254 243 199
    
    # Right Column Bottom: AI 3D Prompt or Exam Tip
    $aiBox = $slide.Shapes.AddShape(5, 395, 418, 545, 106)
    $aiBox.Fill.Solid()
    $aiBox.Fill.ForeColor.RGB = Get-RGB 20 25 40
    $aiBox.Line.ForeColor.RGB = $cBlue
    
    $tbAiHdr = $slide.Shapes.AddTextbox(1, 405, 422, 525, 22)
    if ($data.Type -like "MCQ*") {
        $tbAiHdr.TextFrame.TextRange.Text = "NMMS PYQ परीक्षा टिप (Exam Tip):"
    } else {
        $tbAiHdr.TextFrame.TextRange.Text = [string]$labels.AIPromptHeader
    }
    $tbAiHdr.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbAiHdr.TextFrame.TextRange.Font.Size = 10.5
    $tbAiHdr.TextFrame.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tbAiHdr.TextFrame.TextRange.Font.Color.RGB = Get-RGB 147 197 253
    
    $tbAiTxt = $slide.Shapes.AddTextbox(1, 405, 442, 525, 78)
    $tbAiTxt.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    if ($data.Type -like "MCQ*") {
        $tbAiTxt.TextFrame.TextRange.Text = "$($labels.TeacherExamTip)"
    } else {
        $tbAiTxt.TextFrame.TextRange.Text = [string]$data.AIPrompt
    }
    $tbAiTxt.TextFrame.TextRange.Font.Name = "Segoe UI"
    $tbAiTxt.TextFrame.TextRange.Font.Size = 10
    $tbAiTxt.TextFrame.TextRange.Font.Color.RGB = Get-RGB 226 232 240
}

$teacherPptx = "$baseDir\Teacher_Master_Story_Guide.pptx"
$teacherPdf  = "$baseDir\Teacher_Master_Story_Guide.pdf"
Remove-Item $teacherPptx, $teacherPdf -Force -ErrorAction SilentlyContinue
$presTeacher.SaveAs($teacherPptx)
$presTeacher.SaveAs($teacherPdf, 32)
$presTeacher.Close()
Write-Output "Teacher Master Story Guide Presentation & PDF created successfully!"

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()
Start-Sleep -Seconds 3

# ==============================================================
# POST-PROCESSING: ENSURE 100% MUTED & INDEFINITE LOOPING IN XML
# ==============================================================
Write-Output "`nApplying XML Mute & Infinite Loop guarantee to PPTX files..."
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

function Ensure-MutedAndLooping([string]$targetPptx) {
    if (-not (Test-Path $targetPptx)) { return }
    $zip = [System.IO.Compression.ZipFile]::Open($targetPptx, 2)
    $updated = 0
    foreach ($entry in $zip.Entries) {
        if ($entry.FullName -like 'ppt/slides/slide*.xml') {
            $stream = $entry.Open()
            $reader = New-Object System.IO.StreamReader($stream)
            $content = $reader.ReadToEnd()
            $reader.Close()
            $stream.Close()
            
            if ($content -match '<p:cMediaNode') {
                $newContent = [System.Text.RegularExpressions.Regex]::Replace($content, 'vol="\d+"', 'vol="0" mute="1"')
                $newContent = [System.Text.RegularExpressions.Regex]::Replace($newContent, '(<p:cMediaNode[^>]*><p:cTn\s+[^>]*?repeatCount=")[^"]*(")', '${1}indefinite${2}')
                $newContent = [System.Text.RegularExpressions.Regex]::Replace($newContent, '(<p:cMediaNode[^>]*><p:cTn\s+id="\d+")(?!\s+repeatCount)', '${1} repeatCount="indefinite"')
                
                $stream = $entry.Open()
                $stream.SetLength(0)
                $writer = New-Object System.IO.StreamWriter($stream, [System.Text.Encoding]::UTF8)
                $writer.Write($newContent)
                $writer.Flush()
                $writer.Close()
                $stream.Close()
                $updated++
            }
        }
    }
    $zip.Dispose()
    Write-Output "  XML Mute & Infinite Loop applied to $updated slides in: $(Split-Path $targetPptx -Leaf)"
}

Ensure-MutedAndLooping $studentPptx
Ensure-MutedAndLooping $teacherPptx

Write-Output "`nAll tasks finished! Both PPTX and PDF editions are ready in:`n$baseDir"

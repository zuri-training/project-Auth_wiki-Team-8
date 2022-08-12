<tableViewSection headerTitle = "URL Handler Type (choose one)" id = "rbp-oP-vn0" >
 <cells >
        <tableViewCell clipsSubviews = "YES" contentMode = "scaleToFill" selectionStyle = "blue" hidesAccessoryWhenEditing = "NO" indentationLevel = "1" indentationWidth = "0.0" id = "kY0-iH-aFH" >
            <rect key = "frame" x = "0.0" y = "172" width = "414" height = "44"/>
            <autoresizingMask key = "autoresizingMask"/>
            <tableViewCellContentView key = "contentView" opaque = "NO" clipsSubviews = "YES" multipleTouchEnabled = "YES" contentMode = "center" tableViewCell = "kY0-iH-aFH" id = "gAh-hq-mfA" >
                <rect key = "frame" x = "0.0" y = "0.0" width = "414" height = "44"/>
                <autoresizingMask key = "autoresizingMask"/>
                <subviews >
                    <switch opaque = "NO" contentMode = "scaleToFill" horizontalHuggingPriority = "750" verticalHuggingPriority = "750" contentHorizontalAlignment = "center" contentVerticalAlignment = "center" on = "YES" translatesAutoresizingMaskIntoConstraints = "NO" id = "2QY-0I-Guy" >
                        <rect key = "frame" x = "337" y = "6.5" width = "51" height = "31"/>
                        <connections >
                            <action selector = "urlHandlerChange:" destination = "m6z-f8-zu8" eventType = "valueChanged" id = "ETr-nI-ZPV"/>
                        </connections >
                    </switch >
                    <label opaque = "NO" userInteractionEnabled = "NO" contentMode = "left" horizontalHuggingPriority = "251" verticalHuggingPriority = "251" text = "Open with external web browser" textAlignment = "natural" lineBreakMode = "tailTruncation" baselineAdjustment = "alignBaselines" adjustsFontSizeToFit = "NO" translatesAutoresizingMaskIntoConstraints = "NO" id = "r38-s1-Ams" >
                        <rect key = "frame" x = "28" y = "11.5" width = "246" height = "21"/>
                        <fontDescription key = "fontDescription" type = "system" pointSize = "17"/>
                        <nil key = "highlightedColor"/>
                    </label >
                </subviews >
                <constraints >
                    <constraint firstItem = "2QY-0I-Guy" firstAttribute = "centerY" secondItem = "gAh-hq-mfA" secondAttribute = "centerY" id = "0dj-14-Yma"/>
                    <constraint firstAttribute = "trailingMargin" secondItem = "2QY-0I-Guy" secondAttribute = "trailing" constant = "8" id = "KvC-Cv-n4V"/>
                    <constraint firstItem = "r38-s1-Ams" firstAttribute = "leading" secondItem = "gAh-hq-mfA" secondAttribute = "leadingMargin" constant = "8" id = "el9-nq-KG4"/>
                    <constraint firstItem = "2QY-0I-Guy" firstAttribute = "centerX" secondItem = "gAh-hq-mfA" secondAttribute = "centerX" id = "u1E-jE-Rez"/>
                    <constraint firstItem = "r38-s1-Ams" firstAttribute = "centerY" secondItem = "gAh-hq-mfA" secondAttribute = "centerY" id = "yYL-Cz-lju"/>
                </constraints >
                <variation key = "default" >
                   <mask key = "constraints" >
                      <exclude reference = "u1E-jE-Rez"/>
                    </mask >
                </variation >
            </tableViewCellContentView >
        </tableViewCell >

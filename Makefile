metadata:
	objective-metadata-tool --verbose scan --sdk-root /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk --min-deployment-ver 10.11

localmeta:
	objective-metadata-tool --verbose scan --sdk-root ./MacOSX.sdk --min-deployment-ver 10.11
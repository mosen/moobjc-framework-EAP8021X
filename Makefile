.PHONY: default

default: metadata
	objective-metadata-tool --verbose scan --sdk-root ./MacOSX10.12.sdk --min-deployment-ver 10.11
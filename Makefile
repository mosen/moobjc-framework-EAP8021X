.PHONY: default

default: scan
	objective-metadata-tool --verbose scan --sdk-root ./MacOSX10.12.sdk --min-deployment-ver 10.11

compile:
	objective-metadata-tool --verbose compile
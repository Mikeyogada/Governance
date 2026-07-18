package main 

#ensure an SBOM format exists
deny contains msg if {
	not input.bomFormat
	msg := sprintf("SBOM format is required, but not found in the input: %v", [input])
}
#sprintf is used to format the message with the actual value of input

#only cycloneDX is supported
deny contains msg if {
	input.bomFormat != "CycloneDX"
	msg := sprintf("SBOM format is not supported, only 'CycloneDX' is supported, but found: %v", [input.bomFormat])
} #sprintf is used to format the message with the actual value of input.bomFormat

#ensure at least one component exists
deny contains msg if {
	count(input.components) == 0
	msg := sprintf("SBOM must contain at least one component, but none were found in the input: %v", [input])
}


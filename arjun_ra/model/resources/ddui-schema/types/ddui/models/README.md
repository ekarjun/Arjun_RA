# model/resources/ddui-schema/types/ddui/models

### Resource Types
The UIS2 files for a resource type should be stored in the _types/ddui/views/package.ResourceTypes.typeName_ subdirectory of the specified location, where `package.ResourceTypes.typeName` is the fully-qualified resource type ID of the type schema to describe.

### Domain Types
The UIS2 files for a domain type should be stored in the _domain-types/ddui/views/domain_type_ subdirectory of the specified location, where the `domain_type` is the domain type ID configured for the RA, with all colons (:) replaced with dots (.) (eg. `urn:cyaninc:bp:domain:SAM5620` maps to `domain-types/ddui/views/urn.cyaninc.bp.domain.SAM5620`)
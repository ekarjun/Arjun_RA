# model/resources/ui-schema

Location where the UI schema files for the resource and domain types, and the icon files for the domain type are stored. 

### Resource Types
The UI schema files for the resource types should be stored in the base directory of the specified location. The files should have the naming convention of _package.ResourceTypes.typeName.json_, where `package.ResourceTypes.typeName` is the fully-qualified resource type ID of the type schema to describe.

### Domain Types
The UI schema files for the domain types should be stored in the `domain-types` subdirectory of the location. The files should have the naming convention of _domain_type.json_, where the `domain_type` is the domain type ID configured for the RA, with all colons (:) replaced with dots (.) (ex. `urn:cyaninc:bp:domain:SAM5620` maps to `urn.cyaninc.bp.domain.SAM5620.json`)
# Arjun_RA

Blueplanet applications are built using docker containers.

The main [Dockerfile](./Dockerfile) in this directory builds a base image which is shared by the RA docker [image](./docker/ra/Dockerfile) and the simulator docker [image](./docker/sim/Dockerfile).

## Additional Information

Information about the structure of the project can be found in each directory's README.

- [Arjun_RA](.)
	- [docker](./docker)
		- [/ra](./docker/ra)
		- [/sim](./docker/sim)
	- [scripts](./scripts)
	- [arjun_ra](./arjun_ra)
		- [/config/dev](./arjun_ra/config/dev)
		- [/model](./arjun_ra/model)
			- [/commands](./arjun_ra/model/commands)
				- [tests](./arjun_ra/model/commands/tests)
				- [traps](./arjun_ra/model/commands/traps)
				- [/demo-a/demo-a-1](./arjun_ra/model/commands/demo-a/demo-a-1)
			- [/data](./arjun_ra/model/data)
			- [/graphics](./arjun_ra/model/graphics)
				- [/images](./arjun_ra/model/graphics/images)
					- [/demo-a](./arjun_ra/model/graphics/images/demo-a)
			- [/idmappers](./arjun_ra/model/idmappers)
			- [/schema](./arjun_ra/model/schema)
				- [/models](./arjun_ra/model/schema/models)
			- [/templates](./arjun_ra/model/templates)
				- [/traps](./arjun_ra/model/templates/traps)
			- [/resources](./arjun_ra/model/resources)
				- [/resources/ddui-schema](./arjun_ra/model/resources/ddui-schema)
					- [/resources/ddui-schema/views](./arjun_ra/model/resources/ddui-schema/views)
				- [/resources/definitions](./arjun_ra/model/resources/definitions)
				- [/resources/ui-schema](./arjun_ra/model/resources/ui-schema)
					- [/resources/ui-schema/domain-types](./arjun_ra/model/resources/ui-schema/domain-types)
						- [/resources/ui-schema/domain-types/icons](./arjun_ra/model/resources/ui-schema/domain-types/icons)

export interface HierarchyScopeType {
    equipmentID: string;
    equipmentElementLevel: string;
    equipmentLevel: string;
}

// export interface AnyGenericValueType {
//     currencyID: string;
//     currencyCodeListVersionID: string;
//     encodingCode: string;
//     format: string;
//     characterSetCode: string;
//     listID: string;
//     listAgencyID: string;
//     listAgencyName: string;
//     listName: string;
//     listVersionID: string;
//     languageID: string;
//     languageLocaleID: string;
//     listURI: string;
//     listSchemaURI: string;
//     mimeCode: string;
//     name: string;
//     schemaID: string;
//     schemaName: string;
//     schemaAgencyID: string;
//     schemaAgencyName: string;
//     schemaVersionID: string;
//     schemaDataURI: string;
//     schemaURI: string;
//     unitCode: string;
//     unitCodeListID: string;
//     unitCodeListAgencyID: string;
//     unitCodeListAgencyName: string;
//     unitCodeListVersionID: string;
//     filename: string;
//     uri: string;
// }

// // Defined types are
// // - Permanent: an assembly that is not intended to be split during the production process; 
// // - Transient: a temporary assembly using during production, such as a pallet of different materials or a batch kit.

// export let PriorityType = [
//     1,2,3,4,5
// ]

// export let AssemblyRelationshipType = [
//     "Permanent",
//     "Transient",
//     "Other"
// ]

// // Defines the type of the assembly.
// // Defined types are
// // - physical: the components of the assembly are physically connected or in the same area. 
// // - logical: the components of the assembly are not necessarily physically connected or in the same area. 
// export let AssemblyTypeType = [
//     "Physical",
//     "Logical",
//     "Other"
// ]

// // Defines the type of capability. 
// // Defined values are
// // - Committed: capacity that is committed for future productive use;
// // - Unattainable: capacity that is not attainable for future productive use given the equipment condition, equipment utilization, personnel availability or material availability;
// // - Available: capacity that is available for additional future productive use;
// // - Used: a historical value that defines the portion of the capacity with acceptable quality;
// // - Unused: a historical value that defines the portion of the capacity that was not used or had unacceptable quality; and
// // - Total: the sum of used and unused capability or the sum of available, unattainable and committed capability.
// export let CapabilityType1Type = [
//     "Used",
//     "Unused",
//     "Total",
//     "Committed",
//     "Available",
//     "Unattainable",
//     "Other"
// ]

// // Defines the type of the property. Defined types are
// // - ClassType: the property value is defined for the class and there is no value associated with an instance;
// // - InstanceType: the property value of the class is undefined; and
// // - DefaultType: the property value is defined for the class as the default instance value, but individual instances of the class may redefine specific values.
// export let ClassPropertyTypeType = [
//     "ClassType",
//     "InstanceType",
//     "DefaultType",
//     "Inventory",
//     "Mixed",
//     "Other"
// ]


// // export let DataTypeType = [
// //     "Amount",
// //     "BinaryObject",
// //     "Code",
// //     "DateTime",
// //     "Identifier",
// //     "Indicator",
// //     "Measure",
// //     "Numeric",
// //     "Quantity",
// //     "Text",
// //     "string",
// //     "byte",
// //     "unsignedByte",
// //     "binary",
// //     "integer",
// //     "positiveInteger",
// //     "negativeInteger",
// //     "nonNegativeInteger",
// //     "nonPositiveInteger",
// //     "int",
// //     "unsignedInt",
// //     "long",
// //     "unsignedLong",
// //     "short",
// //     "unsignedShort",
// //     "decimal",
// //     "float",
// //     "double",
// //     "boolean",
// //     "time",
// //     "timeInstant",
// //     "timePeriod",
// //     "duration",
// //     "date",
// //     "dateTime",
// //     "month",
// //     "year",
// //     "century",
// //     "recurringDay",
// //     "recurringDate",
// //     "recurringDuration",
// //     "Name",
// //     "QName",
// //     "NCName",
// //     "uriReference",
// //     "language",
// //     "ID",
// //     "IDREF",
// //     "IDREFS",
// //     "ENTITY",
// //     "ENTITIES",
// //     "NOTATION",
// //     "NMTOKEN",
// //     "NMTOKENS",
// //     "Enumeration",
// //     "SVG",
// //     "Other"
// // ]

// // Defines the type of the definition of a process segment, operations definition, or operations segment. 
// // Defined types are:
// // -	Pattern: a segment or definition used as a template for other segments or definitions;
// // -	Instance: a segment or definition that may be directly scheduled and tracked.
// export let DefinitionTypeType = [
//     "Pattern",
//     "Instance"
// ]

// // Defines an execution dependency constraint of two elements. 
// // Defined values are (explained using dependency type between element A and element B)
// // -	at start: start B at A start;
// // -	after start: start B after A start;
// // -	after end: start B after A end;
// // -	not follow: B cannot follow A;
// // -	possible parallel: B may run in parallel to A;
// // -	not in parallel: B may not run in parallel to A;
// // -	no later after start: start B no later than dependency factor after A start:
// // -	no earlier after start: start B no earlier than dependency factor after A start;
// // -	no later after end: start B no later than dependency factor after A end;
// // -	no earlier after end: B no earlier than dependency factor after A end.
// export let DependencyType = [
//     "NotFollow",
//     "PossibleParallel",
//     "NotInParallel",
//     "AtStart",
//     "AfterStart",
//     "AfterEnd",
//     "NoLaterAfterStart",
//     "NoEarlierAfterStart",
//     "NoLaterAfterEnd",
//     "NoEarlierAfterEnd",
//     "Other"
// ]

// export interface EquipmentAssetMappingType {
//     EquipmentID: string;
//     PhysicalAssetID: string;
//     HierarchyScope: string;
//     StartTime: Date;
//     EndTime: Date;
// }

// // Defines the role based equipment hierarchy level as defined in ISA 95. 
// // Defined values are:
// export let EquipmentElementLevelType = [
//     "Enterprise",
//     "Site",
//     "Area",
//     "ProcessCell",
//     "Unit",
//     "ProductionLine",
//     "WorkCell",
//     "ProductionUnit",
//     "StorageZone",
//     "StorageUnit",
//     "WorkCenter",
//     "WorkUnit",
//     "EquipmentModule",
//     "ControlModule",
//     "Other"
// ]

// // The hierarchy scope identifies where the exchanged information fits within the role-based equipment hierarchy. 
// // It defines the scope of the exchanged information, such as a site or area for which the information is relevant. 
// // The hierarchy scope identifies the associated instance in the role-based equipment hierarchy.
// export interface HierarchyScopeType {
//     EquipmentID: string;
//     EquipmentElementLevel: string;
//     EquipmentLevel: string;
// }

// // Defines the commands to a job order, as defined in ISA 95 and ISA 88.
// // Defined values are:
// export let JobOrderCommandType = [
//     "Start",
//     "Stop",
//     "Hold",
//     "Restart",
//     "Abort",
//     "Reset",
//     "Pause",
//     "Resume",
//     "Other"
// ]

// // Defines the states to a job order, as defined in ISA 95 and ISA 88.
// // Defined values are
// export let JobOrderDispatchStatusType = [
//     "Waiting",
//     "Pending",
//     "Cancelled",
//     "Dispatched",
//     "Ready",
//     "Running",
//     "Completed",
//     "Aborted",
//     "Held",
//     "Suspended",
//     "Closed",
//     "Other"
// ]

// // Defines the expected use of the material class, material definition, material lot, or material sublot in the context of the operations segment.
// // Defined values for production operations are
// // - Consumable, Consumed, Produced, By-product Produced, Co-product Produced, and Yield Produced.

// // Defined values for maintenance operations are
// // - Consumable, Material Consumed, and Material Produced.

// // Defined values for quality test operations are 
// // - Consumable, Destructive Sample, Returned Sample, and Retained Sample.

// // Defined values for inventory operations defined values are
// // - Consumable, Material Consumed, Material Produced, and Inventoried.
// export let MaterialUseType = [
//     "Consumable",
//     "Consumed",
//     "Produced",
//     "By-product Produced",
//     "Co-product Produced",
//     "Yield Produced",
//     "Material Consumed",
//     "Material Produced",
//     "Destructive Sample",
//     "Returned Sample",
//     "Retained Sample",
//     "Inventoried",
//     "Other"
// ]

// export interface OpEquipmentRequirementType {
//     EquipmentClassID: string;
//     EquipmentID: string;
//     Description: string;
//     EquipmentUse: string;
//     Quantity: string;
//     HierarchyScope: string;
//     SpatialDefinition: string;
//     OperationalLocation: string;
//     EquipmentLevel: string;
//     EquipmentRequirementProperty: OpEquipmentRequirementPropertyType[];
//     RequiredByRequestedSegmentResponse: string
//     TestSpecificationID: string;
// }

// export interface OpEquipmentRequirementPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     EquipmentRequirementProperty: OpEquipmentRequirementPropertyType[];
// }

// export interface OpPersonnelRequirementType {
//     PersonnelClassID: string;
//     PersonID: string;
//     Description: string;
//     PersonnelUse: string;
//     Quantity: string;
//     HierarchyScope: string;
//     SpatialDefinition: string;
//     OperationalLocation: string;
//     PersonnelRequirementProperty: OpPersonnelRequirementPropertyType[];
//     RequiredByRequestedSegmentResponse: string;
//     TestSpecificationID: string;
// }

// export interface OpPersonnelRequirementPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     PersonnelRequirementProperty: OpPersonnelRequirementPropertyType[];
// }

// export interface OpPhysicalAssetRequirementType {
//     PhysicalAssetClassID: string;
//     PhysicalAssetID: string;
//     Description: string;
//     PhysicalAssetUse: string;
//     Quantity: string;
//     HierarchyScope: string;
//     SpatialDefinition: string;
//     PhysicalLocation: string;
//     EquipmentLevel: string;
//     PhysicalAssetRequirementProperty: OpPhysicalAssetRequirementPropertyType[];
//     RequiredByRequestedSegmentResponse: string;
//     TestSpecificationID: string;
// }

// export interface OpPhysicalAssetRequirementPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     PhysicalAssetRequirementProperty: OpPhysicalAssetRequirementPropertyType[];
// } 

// export interface OpMaterialRequirementType {
//     MaterialClassID: string;
//     MaterialDefinitionID: string;
//     MaterialLotID: string;
//     MaterialSubLotID: string;
//     Description: string;
//     MaterialUse: string;
//     SpatialDefinition: string;
//     StorageLocation: string;
//     Quantity: string;
//     AssemblyRequirement: OpMaterialRequirementType[];
//     AssemblyType: string;
//     AssemblyRelationship: string;
//     HierarchyScope: string;
//     MaterialRequirementProperty: OpMaterialRequirementPropertyType[];
//     RequiredByRequestedSegmentResponse: string;
//     TestSpecificationID: string;
// }  

// export interface OpMaterialRequirementPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     MaterialRequirementProperty: OpMaterialRequirementPropertyType[];
// }  

// export interface OpPersonnelSpecificationType {
//     PersonnelClassID: string;
//     PersonID: string;
//     Description: string;
//     PersonnelUse: string;
//     HierarchyScope: string;
//     Quantity: string;
//     PersonnelSpecificationProperty: OpPersonnelSpecificationPropertyType[];
//     TestSpecificationID: string;
// }

// export interface OpPersonnelSpecificationPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     PersonnelSpecificationProperty: OpPersonnelSpecificationPropertyType[];
// }  

// export interface OpEquipmentSpecificationType {
//     OpEquipmentSpecificationType: string;
//     EquipmentID: string;
//     Description: string;
//     EquipmentUse: string;
//     HierarchyScope: string;
//     Quantity: string;
//     EquipmentSpecificationProperty: OpEquipmentSpecificationPropertyType[];
//     TestSpecificationID: string;
// }  

// export interface OpEquipmentSpecificationPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     EquipmentSpecificationProperty: OpEquipmentSpecificationPropertyType[];
// }  

// export interface OpPhysicalAssetSpecificationType {
//     PhysicalAssetClassID: string;
//     PhysicalAssetID: string;
//     Description: string;
//     PhysicalAssetUse: string;
//     HierarchyScope: string;
//     Quantity: string;
//     PhysicalAssetSpecificationProperty: OpPhysicalAssetSpecificationPropertyType[];
//     TestSpecificationID: string;
// }  

// export interface OpPhysicalAssetSpecificationPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     PhysicalAssetSpecificationProperty: OpPhysicalAssetSpecificationPropertyType[];
// }  

// export interface OpMaterialSpecificationType {
//     ID: string;
//     MaterialClassID: string;
//     MaterialDefinitionID: string;
//     Description: string;
//     MaterialUse: string;
//     HierarchyScope: string;
//     Quantity: string;
//     AssemblySpecification: OpMaterialSpecificationType[];
//     AssemblyType: string;
//     AssemblyRelationship: string;
//     MaterialSpecificationProperty: OpMaterialSpecificationPropertyType[];
//     TestSpecificationID: string;
// }  

// export interface OpMaterialSpecificationPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     MaterialSpecificationProperty: OpMaterialSpecificationPropertyType[];
// }  

// export interface OpPersonnelCapabilityType {
//     PersonnelClassID: string;
//     PersonID: string;
//     Description: string;
//     CapabilityType: string;
//     Reason: string;
//     ConfidenceFactor: string;
//     HierarchyScope: string;
//     SpatialDefinition: string;
//     OperationalLocation: string;
//     PersonnelUse: string;
//     StartTime: Date;
//     EndTime: Date;
//     Quantity: string;
//     PersonnelCapability: OpPersonnelCapabilityType[];
//     PersonnelCapabilityProperty: OpPersonnelCapabilityPropertyType[];
// }  

// export interface OpPersonnelCapabilityPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     PersonnelCapabilityProperty: OpPersonnelCapabilityPropertyType[];
// }  

// export interface OpEquipmentCapabilityType {
//     EquipmentClassID: string;
//     EquipmentID: string;
//     Description: string;
//     CapabilityType: string;
//     Reason: string;
//     ConfidenceFactor: string;
//     HierarchyScope: string;
//     SpatialDefinition: string;
//     OperationalLocation: string;
//     EquipmentUse: string;
//     StartTime: Date;
//     EndTime: Date;
//     Quantity: string;
//     EquipmentCapability: OpEquipmentCapabilityType[];
//     EquipmentCapabilityProperty: OpEquipmentCapabilityPropertyType[];
// }  

// export interface OpEquipmentCapabilityPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     EquipmentCapabilityProperty: OpEquipmentCapabilityPropertyType[];
// }  

// export interface OpPhysicalAssetCapabilityType {
//     PhysicalAssetClassID: string;
//     PhysicalAssetID: string;
//     Description: string;
//     CapabilityType: string;
//     Reason: string;
//     ConfidenceFactor: string;
//     HierarchyScope: string;
//     SpatialDefinition: string;
//     PhysicalLocation: string;
//     PhysicalAssetUse: string;
//     StartTime: Date;
//     EndTime: Date;
//     Quantity: string;
//     PhysicalAssetCapability: OpPhysicalAssetCapabilityType[];
//     PhysicalAssetCapabilityProperty: OpPhysicalAssetCapabilityPropertyType[];
// }  

// export interface OpPhysicalAssetCapabilityPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     PhysicalAssetCapabilityProperty: OpPhysicalAssetCapabilityPropertyType[];
// }  

// export interface OpMaterialCapabilityType {
//     MaterialClassID: string;
//     MaterialDefinitionID: string;
//     MaterialLotID: string;
//     MaterialSubLotID: string;
//     Description: string;
//     CapabilityType: string;
//     Reason: string;
//     ConfidenceFactor: string;
//     HierarchyScope: string;
//     MaterialUse: string;
//     SpatialDefinition: string;
//     StorageLocation: string;
//     StartTime: Date;
//     EndTime: Date;
//     AssemblyCapability: OpMaterialCapabilityType[];
//     AssemblyType: "";
//     AssemblyRelationship: string;
//     Quantity: string;
//     MaterialCapabilityProperty: OpMaterialCapabilityPropertyType[];
// }  

// export interface OpMaterialCapabilityPropertyType {
//     ID: string;
//     Description: string;
//     Value: string;
//     Quantity: string;
//     MateralCapabilityProperty: OpMaterialCapabilityPropertyType[];
// }
// // Describes the category of the activity. 
// // Defined values are 
// // - Production, Maintenance, Quality, Inventory, or Mixed. 
// // - Mixed” can be used when the activity covers several categories.
// export let OperationsTypeType = [
//     "Production",
//     "Maintenance",
//     "Quality",
//     "Inventory",
//     "Mixed",
//     "Other",
// ]

// export interface ParameterType {
//     ID: string;
//     Value: string;
//     Description: string;
//     HierarchyScope: string;
//     Parameter: string;
// }

// // Indicates the state of an operations or work request. 
// // Defined values are
// export let RequestStateType = [
//     "Forecast",
//     "Released",
//     "Cancelled",
//     "Ready",
//     "Running",
//     "Completed",
//     "Aborted",
//     "Held",
//     "Paused",
//     "Closed",
//     "Other",
// ]

// // Indicates whether the storage location attribute refers to an operational location, equipment 
// // or physical asset object, or contains a description of the storage location.
// // Mandatory where a storage location is specified.
// // Defined values are
// // -	Operational Location: 	storage location attribute references an operational location (OperationalLocationID);
// // -	Equipment: 				storage location attribute references an equipment object (EquipmentID);
// // -	Physical Asset: 		storage location attribute references a physical asset (PhysicalAssetID); and
// // -	Description: 			storage location attribute contains a description of the storage location, such as a street address.
// export let ResourceLocationTypeType = [
//    "Operational Location",
//    "Equipment",
//    "Physical Asset",
//    "Description",
//    "Other"
// ]

// // Indicates the type of the resource referenced. 
// // Defined values are
// export let ResourceReferenceTypeType =[
//     "Personnel",
//     "Personnel Class",
//     "Equipment",
//     "Equipment Class",
//     "Material Class",
//     "Material Definition",
//     "Material Lot",
//     "Material Sublot",
//     "Physical Asset",
//     "Physical Asset Class",
//     "Work Master",
//     "Process Segment",
//     "Other", 
// ]

// // Defines the states to a operations response.
// // Defined values are
// export let ResponseStateType = [
//     "Ready",
//     "Running",
//     "Completed",
//     "Aborted",
//     "Holding",
//     "Paused",
//     "Other",
// ]

// export let UnitOfMeasureType = [
//     {"Name":"degrees C", "Description": "degrees Celsius"},
//     {"Name":"degrees F", "Description": "degrees Fahrenheit"},
//     {"Name":"A", "Description": "ampere(s)"},
//     {"Name":"atm", "Description": "standard atmosphere"},
//     {"Name":"AU", "Description": "astronomical unit"},
//     {"Name":"bbl", "Description": "barrel(s)"},
//     {"Name":"Bcf", "Description": "billion cubic feet (gas flow)"},
//     {"Name":"Bcfd", "Description": "billion cubic feet per day (gas flow)"},
//     {"Name":"Bcfy", "Description": "billion cubic feet per year (gas flow)"},
//     {"Name":"Btu", "Description": "British thermal unit(s)"},
//     {"Name":"Bunit", "Description": "billion unit(s)"},
//     {"Name":"c", "Description": "cycle(s)"},
//     {"Name":"c", "Description": "centi (one-hundredth); prefix only"},
//     {"Name":"C", "Description": "coulomb(s)"},
//     {"Name":"cal ", "Description": "calorie(s)"},
//     {"Name":"cd", "Description": "candela(s)"},
//     {"Name":"Ci ", "Description": "curie(s)"},
//     {"Name":"cmil", "Description": "circular mil"},
//     {"Name":"cp", "Description": "candlepower"},
//     {"Name":"cpm", "Description": "count(s) per minute"},
//     {"Name":"cps", "Description": "count(s) per second"},
//     {"Name":"d ", "Description": "day(s)"},
//     {"Name":"d", "Description": "deci (one-tenth); prefix only"},
//     {"Name":"D", "Description": "darcy(s)"},
//     {"Name":"dB", "Description": "decibel(s)"},
//     {"Name":"dyn", "Description": "dyne(s)"},
//     {"Name":"eV ", "Description": "electron volt(s)"},
//     {"Name":"F", "Description": "fermi(s)"},
//     {"Name":"F ", "Description": "farad(s)"},
//     {"Name":"fc", "Description": " footcandle(s)"},
//     {"Name":"fl oz", "Description": "fluid ounce(s)"},
//     {"Name":"ft ", "Description": " foot/feet"},
//     {"Name":"ft/s", "Description": "foot/feet per second"},
//     {"Name":"ft<sup>2</sup>", "Description": "square foot/feet"},
//     {"Name":"ft-lbf", "Description": "foot pound(s) (force)"},
//     {"Name":"g ", "Description": "gram(s)"},
//     {"Name":"g/t ", "Description": "gram(s) per tonne"},
//     {"Name":"g, G", "Description": "Gal (gravity constant)"},
//     {"Name":"G ", "Description": "giga (one billion); prefix only"},
//     {"Name":"gal", "Description": "gallon(s)"},
//     {"Name":"Gs", "Description": "gauss"},
//     {"Name":"h", "Description": "hour(s)"},
//     {"Name":"ha ", "Description": "hectare(s)"},
//     {"Name":"H.E.", "Description": "high explosive(s)"},
//     {"Name":"hp", "Description": " horsepower"},
//     {"Name":"hp-h", "Description": "horsepower hour"},
//     {"Name":"Hz", "Description": "cycle(s) per second"},
//     {"Name":"in Hg", "Description": "inch(es) of mercury"},
//     {"Name":"in", "Description": "inch(es)"},
//     {"Name":"in H<sub>2</sub>O", "Description": "inch(es) of water"},
//     {"Name":"J", "Description": "joule(s)"},
//     {"Name":"k", "Description": "kilo (one thousand); prefix only"},
//     {"Name":"K", "Description": "kelvin"},
//     {"Name":"l", "Description": "liter(s)"},
//     {"Name":"L", "Description": "liter(s) (preferred form)"},
//     {"Name":"L", "Description": "lambert(s)"},
//     {"Name":"lb ", "Description": "pound(s)"},
//     {"Name":"lbf", "Description": "pound(s) force"},
//     {"Name":"lbf-ft", "Description": "pound(s) force foot"},
//     {"Name":"lt", "Description": "long ton(s)"},
//     {"Name":"m", "Description": "meter"},
//     {"Name":"m", "Description": "milli (one-thousandth); prefix only"},
//     {"Name":"M", "Description": "mega (one million)"},
//     {"Name":"Mcf", "Description": "thousand cubic feet (gas flow)"},
//     {"Name":"Mcfd", "Description": "thousand cubic feet per day"},
//     {"Name":"mho", "Description": "mho(s)"},
//     {"Name":"mi", "Description": "mile(s)"},
//     {"Name":"mil", "Description": "thousandth of an inch"},
//     {"Name":"MMbbl", "Description": "million barrels"},
//     {"Name":"MMcf", "Description": "million cubic feet (gas flow)"},
//     {"Name":"MMcfd", "Description": "million cubic feet per day (gas flow)"},
//     {"Name":"MMcfy", "Description": "million cubic feet per year (gas flow)"},
//     {"Name":"mol", "Description": "mole(s)"},
//     {"Name":"mol wt", "Description": "mole weight"},
//     {"Name":"mol %", "Description": "mole percent"},
//     {"Name":"mpg", "Description": "mile(s) per gallon"},
//     {"Name":"mph", "Description": "mile(s) per hour"},
//     {"Name":"Mx", "Description": "maxwell(s)"},
//     {"Name":"n", "Description": "nano (one-billionth); prefix only"},
//     {"Name":"n", "Description": "refractive index"},
//     {"Name":"N", "Description": "Newton(s)"},
//     {"Name":"nmi", "Description": "nautical mile(s)"},
//     {"Name":"Oe", "Description": "oersted(s)"},
//     {"Name":"ohm-cmil/ft", "Description": "ohm circular mil per foot"},
//     {"Name":"oz", "Description": "ounce(s)"},
//     {"Name":"p", "Description": "pico (one-trillionth); prefix only"},
//     {"Name":"P", "Description": "poise(s)"},
//     {"Name":"Pa", "Description": "pascal(s)"},
//     {"Name":"pct", "Description": "percent"},
//     {"Name":"ppb", "Description": "part(s) per billion"},
//     {"Name":"ppm", "Description": "part(s) per million"},
//     {"Name":"psi", "Description": "pound(s) (force) per square inch"},
//     {"Name":"psia", "Description": "pound(s) force per square inch, absolute"},
//     {"Name":"psig", "Description": "pound(s) force per square inch, gauge"},
//     {"Name":"r", "Description": "revolution(s)"},
//     {"Name":"R", "Description": "roentgen(s)"},
//     {"Name":"rad", "Description": "radian(s)"},
//     {"Name":"rpm", "Description": "revolutions per minute"},
//     {"Name":"s", "Description": "second(s)"},
//     {"Name":"S", "Description": "siemens(s)"},
//     {"Name":"sr", "Description": "steradian(s)"},
//     {"Name":"st", "Description": "stere(s)"},
//     {"Name":"st", "Description": "short ton(s)"},
//     {"Name":"St", "Description": "stokes"},
//     {"Name":"std ft<sup>3</sup>", "Description": "standard cubic foot/feet"},
//     {"Name":"t", "Description": "metric ton(s)"},
//     {"Name":"t/w-h", "Description": "metric ton(s) per worker hour"},
//     {"Name":"t/w-d", "Description": "metric ton(s) per worker day"},
//     {"Name":"T", "Description": "tesla(s)"},
//     {"Name":"tr oz", "Description": "troy ounce(s)"},
//     {"Name":"unit<sup>-1</sup>", "Description": "reciprocal unit"},
//     {"Name":"unit<sup>2</sup>", "Description": "square unit (or unit squared)"},
//     {"Name":"unit<sup>3</sup>", "Description": "cubic unit"},
//     {"Name":"W", "Description": "watt(s)"},
//     {"Name":"kW", "Description": "Kilowatt(s)"},
//     {"Name":"MW", "Description": "Megawatt(s)"},
//     {"Name":"Wb", "Description": "weber(s)"},
//     {"Name":"wt %, wt pct", "Description": "weight percent"},
//     {"Name":"yd", "Description": "yard(s)"},
//     {"Name":"yr", "Description": "year(s)"},
// ]


// export let HierarchyScopeType = [
//     {"Parent": "", "Name": "Enterprise"}, 
//     {"Parent": "Enterprise", "Name": "Site"}, 
//     {"Parent": "Site", "Name": "Area"}, 
//     {"Parent": "Area", "Name": "ProcessCell"}, 
//     {"Parent": "ProductionUnit", "Name": "Unit"}, 
//     {"Parent": "Area", "Name": "ProductionLine"}, 
//     {"Parent": "ProductionLine", "Name": "WorkCell"}, 
//     {"Parent": "Area", "Name": "ProductionUnit"}, 
//     {"Parent": "Area", "Name": "StorageZone"},
//     {"Parent": "StorageZone", "Name": "StorageUnit"}, 
//     {"Parent": "ProductionLine", "Name": "WorkCenter"}, 
//     {"Parent": "ProductionUnit", "Name": "WorkUnit"}, 
//     {"Parent": "test", "Name": "EquipmentModule"}, 
//     {"Parent": "test", "Name": "ControlModule"},
//     {"Parent": "test", "Name": "Other"}
// ]

// export let DataTypeType = [
//     {
//         "Name": "Binary",
//         "Description": "Binary is a finite sequence of binary digits (bits)."
//     },
//     {
//         "Name": "Boolean",
//         "Description": "Boolean denotes a logical condition through a predefined enumeration of the literals true (The Boolean condition is satisfied) and false (The Boolean condition is not satisfied).."
//     },
//     {
//         "Name": "Decimal",
//         "Description": "Decimal is a subset of the real numbers, which can be represented by decimal numerals."
//     },
//     {
//         "Name": "Double",
//         "Description": "Double is the IEEE double precision 64 bits floating point type."
//     },
//     {
//         "Name": "Float",
//         "Description": "Float is the IEEE simple precision 32 bits floating point type."
//     },
//     {
//         "Name": "Integer",
//         "Description": "Integer is a value in the infinite set (...-2, -1, 0, 1, 2...), a denumerably infinite list."
//     },
//     {
//         "Name": "String",
//         "Description": "String is a sequence of characters in some suitable character set."
//     },
//     {
//         "Name": "TimeDuration",
//         "Description": "TimeDuration identifies a length of time in various time units as used in the Gregorian calendar: year, month, week, day, hour, minute, second, and fractions thereof. ."
//     },
//     {
//         "Name": "TimePoint",
//         "Description": "TimePoint is a point in time to various common resolutions: year, month, week, day, hour, minute, second, and fractions thereof.."
//     }, 
//     {
//         "Name": "Token",
//         "Description": "A token is a string that does not contain the line feed (#xA) nor tab (#x9) characters, that have no leading or trailing spaces (#x20) and that have no internal sequences of two or more spaces.."
//     },
//     {
//         "Name": "Enumeration",
//         "Description": "Defines a specified set of values."
//     },
//     {
//         "Name": "FractionalDigits",
//         "Description": "Defines the maximum number of fractional digits to be used."
//     },
//     {
//         "Name": "Length",
//         "Description": "Defines the number of units of length of the data type."
//     },
//     {
//         "Name": "MaximumExclusive",
//         "Description": "Defines the upper limit of the range of allowed values. The upper limit is no allowed value.."
//     },
//     {
//         "Name": "MaximumInclusive",
//         "Description": "Defines the upper limit of the range of allowed values. The upper limit is also an allowed value."
//     },
//     {
//         "Name": "MaximumLength",
//         "Description": "Defines the maximum number of units of length."
//     },
//     {
//         "Name": "MinimumLength",
//         "Description": "Defines the minimum number of units of length."
//     },
//     {
//         "Name": "MinimumExclusive",
//         "Description": "Defines the lower limit of the range of allowed values. The lower limit is no allowed value."
//     },
//     {
//         "Name": "MinimumInclusive",
//         "Description": "Defines the lower limit of the range of allowed values. The lower limit is also an allowed value."
//     },
//     {
//         "Name": "Pattern",
//         "Description": "Defines a constraint on the lexical space of a datatype to literals in a specific pattern."
//     },
//     {
//         "Name": "TotalDigits",
//         "Description": "Defines a maximum number of digits to be used."
//     },
//     {
//         "Name": "Amount",
//         "Description": "An amount is a number of monetary units specified in a currency."
//     },
//     {
//         "Name": "Code",
//         "Description": "A code is a character string of letters, numbers, special characters (except escape sequences), and symbols. It represents a definitive value, a method, or a property description in an abbreviated or language-independent form that is part of a finite list of allowed values."
//     },
//     {
//         "Name": "Date",
//         "Description": "A date is a Gregorian calendar representation in various common resolutions: year, month, week, day."

//     },
//     {
//         "Name": "DateTime",
//         "Description": "A date time identifies a date and time of day to various common resolutions: year, month, week, day, hour, minute, second, and fraction of second."
//     },
//     {
//         "Name": "Duration",
//         "Description": "A duration is the specification of a length of time without a fixed start or end time, expressed in Gregorian calendar time units (Year, Month, Week, Day) and Hours, Minutes or Seconds."
//     },
//     {
//         "Name": "Graphic",
//         "Description": "A graphic is a diagram, a graph, mathematical curves, or similar vector based representation in binary notation (octets)."
//     },
//     {
//         "Name": "Identifier",
//         "Description": "An identifier is a character string used to uniquely identify one instance of an object within an identification scheme that is managed by an agency."
//     },
//     {
//         "Name": "Indicator",
//         "Description": "An indicator is a list of two mutually exclusive Boolean values that express the only possible states of a property."
//     },
//     {
//         "Name": "Measure",
//         "Description": "A measure is a numeric value determined by measuring an object along with the specified unit of measure."
//     },
//     {
//         "Name": "Name",
//         "Description": "A name is a word or phrase that constitutes the distinctive designation of a person, place, thing or concept.."

//     },
//     {
//         "Name": "Number",
//         "Description": "A mathematical number that is assigned or is determined by calculation.."
//     },
//     {
//         "Name": "Ordinal",
//         "Description": "An ordinal number is an assigned mathematical number that represents order or sequence."
//     },
//     {
//         "Name": "Percent",
//         "Description": "A percent is a value representing a fraction of one hundred, expressed as a quotient."

//     },
//     {
//         "Name": "Picture",
//         "Description": "A picture is a visual representation of a person, object, or scene in binary notation (octets)."
//     },
//     {
//         "Name": "Quantity",
//         "Description": "A quantity is a counted number of non-monetary units, possibly including fractions."
//     },
//     {
//         "Name": "Rate",
//         "Description": "A rate is a quantity, amount, frequency, or dimensionless factor, measured against an independent base unit, expressed as a quotient."
//     },
//     {
//         "Name": "Ratio",
//         "Description": "A ratio is a relation between two independent quantities, using the same unit of measure or currency. A ratio can be expressed as either a quotient showing the number of times one value contains or is contained within the other, or as a proportion."
//     },
//     {
//         "Name": "Sound",
//         "Description": "A sound is any form of an audio file such as audio recordings in binary notation (octets)."
//     },
//     {
//         "Name": "Text",
//         "Description": "Text is a character string such as a finite set of characters generally in the form of words of a language."
//     },
//     {
//         "Name": "Time",
//         "Description": "Time is a time of day to various common resolutions – hour, minute, second and fractions thereof."
//     },
//     {
//         "Name": "Value",
//         "Description": "A value is the concept of worth in general that is assigned or is determined by measurement, assessment or calculation."
//     },
//     {
//         "Name": "Video",
//         "Description": "A video is a recording, reproducing or broadcasting of visual images on magnetic tape or digitally in binary notation (octets)."
//     }
// ]
// // Describes the category of the activity. 
// // Defined values are 
// // - Production, Maintenance, Quality, Inventory, or Mixed. 
// // - Mixed” can be used when the activity covers several categories.
// export enum OperationsType1Type {
//     "Production",
//     "Maintenance",
//     "Quality",
//     "Inventory",
//     "Mixed",
//     "Other"
// }

// export enum RequestState1Type {
//     "Forecast",
//     "Released",
//     "Cancelled",
//     "Ready",
//     "Running",
//     "Completed",
//     "Aborted",
//     "Held",
//     "Paused",
//     "Closed",
//     "Other"
// }


// export interface QuantityValueType {
//     QuantityString: string;
//     DataType: string;
//     UnitOfMeasure: string;
// }

// export interface ValueType {
//     ValueString: string;
//     DataType: string;
//     UnitOfMeasure: string;
//     Key: string;
// }
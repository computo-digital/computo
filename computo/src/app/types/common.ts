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


export let DataTypeType = [
    "Amount",
    "BinaryObject",
    "Code",
    "DateTime",
    "Identifier",
    "Indicator",
    "Measure",
    "Numeric",
    "Quantity",
    "Text",
    "string",
    "byte",
    "unsignedByte",
    "binary",
    "integer",
    "positiveInteger",
    "negativeInteger",
    "nonNegativeInteger",
    "nonPositiveInteger",
    "int",
    "unsignedInt",
    "long",
    "unsignedLong",
    "short",
    "unsignedShort",
    "decimal",
    "float",
    "double",
    "boolean",
    "time",
    "timeInstant",
    "timePeriod",
    "duration",
    "date",
    "dateTime",
    "month",
    "year",
    "century",
    "recurringDay",
    "recurringDate",
    "recurringDuration",
    "Name",
    "QName",
    "NCName",
    "uriReference",
    "language",
    "ID",
    "IDREF",
    "IDREFS",
    "ENTITY",
    "ENTITIES",
    "NOTATION",
    "NMTOKEN",
    "NMTOKENS",
    "Enumeration",
    "SVG",
    "Other"
]

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
export let EquipmentElementLevelType = [
    "Enterprise",
    "Site",
    "Area",
    "ProcessCell",
    "Unit",
    "ProductionLine",
    "WorkCell",
    "ProductionUnit",
    "StorageZone",
    "StorageUnit",
    "WorkCenter",
    "WorkUnit",
    "EquipmentModule",
    "ControlModule",
    "Other"
]

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

export let UnitOfMeasureType = [
    {"value":"degrees C", "description": "degrees Celsius"},
    {"value":"degrees F", "description": "degrees Fahrenheit"},
    {"value":"A", "description": "ampere(s)"},
    {"value":"atm", "description": "standard atmosphere"},
    {"value":"AU", "description": "astronomical unit"},
    {"value":"bbl", "description": "barrel(s)"},
    {"value":"Bcf", "description": "billion cubic feet (gas flow)"},
    {"value":"Bcfd", "description": "billion cubic feet per day (gas flow)"},
    {"value":"Bcfy", "description": "billion cubic feet per year (gas flow)"},
    {"value":"Btu", "description": "British thermal unit(s)"},
    {"value":"Bunit", "description": "billion unit(s)"},
    {"value":"c", "description": "cycle(s)"},
    {"value":"c", "description": "centi (one-hundredth); prefix only"},
    {"value":"C", "description": "coulomb(s)"},
    {"value":"cal ", "description": "calorie(s)"},
    {"value":"cd", "description": "candela(s)"},
    {"value":"Ci ", "description": "curie(s)"},
    {"value":"cmil", "description": "circular mil"},
    {"value":"cp", "description": "candlepower"},
    {"value":"cpm", "description": "count(s) per minute"},
    {"value":"cps", "description": "count(s) per second"},
    {"value":"d ", "description": "day(s)"},
    {"value":"d", "description": "deci (one-tenth); prefix only"},
    {"value":"D", "description": "darcy(s)"},
    {"value":"dB", "description": "decibel(s)"},
    {"value":"dyn", "description": "dyne(s)"},
    {"value":"eV ", "description": "electron volt(s)"},
    {"value":"F", "description": "fermi(s)"},
    {"value":"F ", "description": "farad(s)"},
    {"value":"fc", "description": " footcandle(s)"},
    {"value":"fl oz", "description": "fluid ounce(s)"},
    {"value":"ft ", "description": " foot/feet"},
    {"value":"ft/s", "description": "foot/feet per second"},
    {"value":"ft<sup>2</sup>", "description": "square foot/feet"},
    {"value":"ft-lbf", "description": "foot pound(s) (force)"},
    {"value":"g ", "description": "gram(s)"},
    {"value":"g/t ", "description": "gram(s) per tonne"},
    {"value":"g, G", "description": "Gal (gravity constant)"},
    {"value":"G ", "description": "giga (one billion); prefix only"},
    {"value":"gal", "description": "gallon(s)"},
    {"value":"Gs", "description": "gauss"},
    {"value":"h", "description": "hour(s)"},
    {"value":"ha ", "description": "hectare(s)"},
    {"value":"H.E.", "description": "high explosive(s)"},
    {"value":"hp", "description": " horsepower"},
    {"value":"hp-h", "description": "horsepower hour"},
    {"value":"Hz", "description": "cycle(s) per second"},
    {"value":"in Hg", "description": "inch(es) of mercury"},
    {"value":"in", "description": "inch(es)"},
    {"value":"in H<sub>2</sub>O", "description": "inch(es) of water"},
    {"value":"J", "description": "joule(s)"},
    {"value":"k", "description": "kilo (one thousand); prefix only"},
    {"value":"K", "description": "kelvin"},
    {"value":"l", "description": "liter(s)"},
    {"value":"L", "description": "liter(s) (preferred form)"},
    {"value":"L", "description": "lambert(s)"},
    {"value":"lb ", "description": "pound(s)"},
    {"value":"lbf", "description": "pound(s) force"},
    {"value":"lbf-ft", "description": "pound(s) force foot"},
    {"value":"lt", "description": "long ton(s)"},
    {"value":"m", "description": "meter"},
    {"value":"m", "description": "milli (one-thousandth); prefix only"},
    {"value":"M", "description": "mega (one million)"},
    {"value":"Mcf", "description": "thousand cubic feet (gas flow)"},
    {"value":"Mcfd", "description": "thousand cubic feet per day"},
    {"value":"mho", "description": "mho(s)"},
    {"value":"mi", "description": "mile(s)"},
    {"value":"mil", "description": "thousandth of an inch"},
    {"value":"MMbbl", "description": "million barrels"},
    {"value":"MMcf", "description": "million cubic feet (gas flow)"},
    {"value":"MMcfd", "description": "million cubic feet per day (gas flow)"},
    {"value":"MMcfy", "description": "million cubic feet per year (gas flow)"},
    {"value":"mol", "description": "mole(s)"},
    {"value":"mol wt", "description": "mole weight"},
    {"value":"mol %", "description": "mole percent"},
    {"value":"mpg", "description": "mile(s) per gallon"},
    {"value":"mph", "description": "mile(s) per hour"},
    {"value":"Mx", "description": "maxwell(s)"},
    {"value":"n", "description": "nano (one-billionth); prefix only"},
    {"value":"n", "description": "refractive index"},
    {"value":"N", "description": "Newton(s)"},
    {"value":"nmi", "description": "nautical mile(s)"},
    {"value":"Oe", "description": "oersted(s)"},
    {"value":"ohm-cmil/ft", "description": "ohm circular mil per foot"},
    {"value":"oz", "description": "ounce(s)"},
    {"value":"p", "description": "pico (one-trillionth); prefix only"},
    {"value":"P", "description": "poise(s)"},
    {"value":"Pa", "description": "pascal(s)"},
    {"value":"pct", "description": "percent"},
    {"value":"ppb", "description": "part(s) per billion"},
    {"value":"ppm", "description": "part(s) per million"},
    {"value":"psi", "description": "pound(s) (force) per square inch"},
    {"value":"psia", "description": "pound(s) force per square inch, absolute"},
    {"value":"psig", "description": "pound(s) force per square inch, gauge"},
    {"value":"r", "description": "revolution(s)"},
    {"value":"R", "description": "roentgen(s)"},
    {"value":"rad", "description": "radian(s)"},
    {"value":"rpm", "description": "revolutions per minute"},
    {"value":"s", "description": "second(s)"},
    {"value":"S", "description": "siemens(s)"},
    {"value":"sr", "description": "steradian(s)"},
    {"value":"st", "description": "stere(s)"},
    {"value":"st", "description": "short ton(s)"},
    {"value":"St", "description": "stokes"},
    {"value":"std ft<sup>3</sup>", "description": "standard cubic foot/feet"},
    {"value":"t", "description": "metric ton(s)"},
    {"value":"t/w-h", "description": "metric ton(s) per worker hour"},
    {"value":"t/w-d", "description": "metric ton(s) per worker day"},
    {"value":"T", "description": "tesla(s)"},
    {"value":"tr oz", "description": "troy ounce(s)"},
    {"value":"unit<sup>-1</sup>", "description": "reciprocal unit"},
    {"value":"unit<sup>2</sup>", "description": "square unit (or unit squared)"},
    {"value":"unit<sup>3</sup>", "description": "cubic unit"},
    {"value":"W", "description": "watt(s)"},
    {"value":"kW", "description": "Kilowatt(s)"},
    {"value":"MW", "description": "Megawatt(s)"},
    {"value":"Wb", "description": "weber(s)"},
    {"value":"wt %, wt pct", "description": "weight percent"},
    {"value":"yd", "description": "yard(s)"},
    {"value":"yr", "description": "year(s)"},
]


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
//         "description": "Binary is a finite sequence of binary digits (bits)."
//     },
//     {
//         "Name": "Boolean",
//         "description": "Boolean denotes a logical condition through a predefined enumeration of the literals true (The Boolean condition is satisfied) and false (The Boolean condition is not satisfied).."
//     },
//     {
//         "Name": "Decimal",
//         "description": "Decimal is a subset of the real numbers, which can be represented by decimal numerals."
//     },
//     {
//         "Name": "Double",
//         "description": "Double is the IEEE double precision 64 bits floating point type."
//     },
//     {
//         "Name": "Float",
//         "description": "Float is the IEEE simple precision 32 bits floating point type."
//     },
//     {
//         "Name": "Integer",
//         "description": "Integer is a value in the infinite set (...-2, -1, 0, 1, 2...), a denumerably infinite list."
//     },
//     {
//         "Name": "String",
//         "description": "String is a sequence of characters in some suitable character set."
//     },
//     {
//         "Name": "TimeDuration",
//         "description": "TimeDuration identifies a length of time in various time units as used in the Gregorian calendar: year, month, week, day, hour, minute, second, and fractions thereof. ."
//     },
//     {
//         "Name": "TimePoint",
//         "description": "TimePoint is a point in time to various common resolutions: year, month, week, day, hour, minute, second, and fractions thereof.."
//     }, 
//     {
//         "Name": "Token",
//         "description": "A token is a string that does not contain the line feed (#xA) nor tab (#x9) characters, that have no leading or trailing spaces (#x20) and that have no internal sequences of two or more spaces.."
//     },
//     {
//         "Name": "Enumeration",
//         "description": "Defines a specified set of values."
//     },
//     {
//         "Name": "FractionalDigits",
//         "description": "Defines the maximum number of fractional digits to be used."
//     },
//     {
//         "Name": "Length",
//         "description": "Defines the number of units of length of the data type."
//     },
//     {
//         "Name": "MaximumExclusive",
//         "description": "Defines the upper limit of the range of allowed values. The upper limit is no allowed value.."
//     },
//     {
//         "Name": "MaximumInclusive",
//         "description": "Defines the upper limit of the range of allowed values. The upper limit is also an allowed value."
//     },
//     {
//         "Name": "MaximumLength",
//         "description": "Defines the maximum number of units of length."
//     },
//     {
//         "Name": "MinimumLength",
//         "description": "Defines the minimum number of units of length."
//     },
//     {
//         "Name": "MinimumExclusive",
//         "description": "Defines the lower limit of the range of allowed values. The lower limit is no allowed value."
//     },
//     {
//         "Name": "MinimumInclusive",
//         "description": "Defines the lower limit of the range of allowed values. The lower limit is also an allowed value."
//     },
//     {
//         "Name": "Pattern",
//         "description": "Defines a constraint on the lexical space of a datatype to literals in a specific pattern."
//     },
//     {
//         "Name": "TotalDigits",
//         "description": "Defines a maximum number of digits to be used."
//     },
//     {
//         "Name": "Amount",
//         "description": "An amount is a number of monetary units specified in a currency."
//     },
//     {
//         "Name": "Code",
//         "description": "A code is a character string of letters, numbers, special characters (except escape sequences), and symbols. It represents a definitive value, a method, or a property description in an abbreviated or language-independent form that is part of a finite list of allowed values."
//     },
//     {
//         "Name": "Date",
//         "description": "A date is a Gregorian calendar representation in various common resolutions: year, month, week, day."

//     },
//     {
//         "Name": "DateTime",
//         "description": "A date time identifies a date and time of day to various common resolutions: year, month, week, day, hour, minute, second, and fraction of second."
//     },
//     {
//         "Name": "Duration",
//         "description": "A duration is the specification of a length of time without a fixed start or end time, expressed in Gregorian calendar time units (Year, Month, Week, Day) and Hours, Minutes or Seconds."
//     },
//     {
//         "Name": "Graphic",
//         "description": "A graphic is a diagram, a graph, mathematical curves, or similar vector based representation in binary notation (octets)."
//     },
//     {
//         "Name": "Identifier",
//         "description": "An identifier is a character string used to uniquely identify one instance of an object within an identification scheme that is managed by an agency."
//     },
//     {
//         "Name": "Indicator",
//         "description": "An indicator is a list of two mutually exclusive Boolean values that express the only possible states of a property."
//     },
//     {
//         "Name": "Measure",
//         "description": "A measure is a numeric value determined by measuring an object along with the specified unit of measure."
//     },
//     {
//         "Name": "Name",
//         "description": "A name is a word or phrase that constitutes the distinctive designation of a person, place, thing or concept.."

//     },
//     {
//         "Name": "Number",
//         "description": "A mathematical number that is assigned or is determined by calculation.."
//     },
//     {
//         "Name": "Ordinal",
//         "description": "An ordinal number is an assigned mathematical number that represents order or sequence."
//     },
//     {
//         "Name": "Percent",
//         "description": "A percent is a value representing a fraction of one hundred, expressed as a quotient."

//     },
//     {
//         "Name": "Picture",
//         "description": "A picture is a visual representation of a person, object, or scene in binary notation (octets)."
//     },
//     {
//         "Name": "Quantity",
//         "description": "A quantity is a counted number of non-monetary units, possibly including fractions."
//     },
//     {
//         "Name": "Rate",
//         "description": "A rate is a quantity, amount, frequency, or dimensionless factor, measured against an independent base unit, expressed as a quotient."
//     },
//     {
//         "Name": "Ratio",
//         "description": "A ratio is a relation between two independent quantities, using the same unit of measure or currency. A ratio can be expressed as either a quotient showing the number of times one value contains or is contained within the other, or as a proportion."
//     },
//     {
//         "Name": "Sound",
//         "description": "A sound is any form of an audio file such as audio recordings in binary notation (octets)."
//     },
//     {
//         "Name": "Text",
//         "description": "Text is a character string such as a finite set of characters generally in the form of words of a language."
//     },
//     {
//         "Name": "Time",
//         "description": "Time is a time of day to various common resolutions – hour, minute, second and fractions thereof."
//     },
//     {
//         "Name": "Value",
//         "description": "A value is the concept of worth in general that is assigned or is determined by measurement, assessment or calculation."
//     },
//     {
//         "Name": "Video",
//         "description": "A video is a recording, reproducing or broadcasting of visual images on magnetic tape or digitally in binary notation (octets)."
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

export interface ValueType {
    ValueString: string;
    DataType: string;
    UnitOfMeasure: string;
    Key: string;
}
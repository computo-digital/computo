from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

__NAMESPACE__ = "http://www.mesa.org/xml/B2MML"


@dataclass
class AnyGenericValueType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    currency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyID",
            "type": "Attribute",
        }
    )
    currency_code_list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyCodeListVersionID",
            "type": "Attribute",
        }
    )
    encoding_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "encodingCode",
            "type": "Attribute",
        }
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    character_set_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "characterSetCode",
            "type": "Attribute",
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        }
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        }
    )
    list_agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyName",
            "type": "Attribute",
        }
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        }
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        }
    )
    language_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "languageID",
            "type": "Attribute",
        }
    )
    language_locale_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "languageLocaleID",
            "type": "Attribute",
        }
    )
    list_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "listURI",
            "type": "Attribute",
        }
    )
    list_schema_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "listSchemaURI",
            "type": "Attribute",
        }
    )
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    schema_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaID",
            "type": "Attribute",
        }
    )
    schema_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaName",
            "type": "Attribute",
        }
    )
    schema_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaAgencyID",
            "type": "Attribute",
        }
    )
    schema_agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaAgencyName",
            "type": "Attribute",
        }
    )
    schema_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaVersionID",
            "type": "Attribute",
        }
    )
    schema_data_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaDataURI",
            "type": "Attribute",
        }
    )
    schema_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaURI",
            "type": "Attribute",
        }
    )
    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        }
    )
    unit_code_list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListID",
            "type": "Attribute",
        }
    )
    unit_code_list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListAgencyID",
            "type": "Attribute",
        }
    )
    unit_code_list_agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListAgencyName",
            "type": "Attribute",
        }
    )
    unit_code_list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCodeListVersionID",
            "type": "Attribute",
        }
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class AssemblyRelationship1Type(Enum):
    PERMANENT = "Permanent"
    TRANSIENT = "Transient"
    OTHER = "Other"


class AssemblyType1Type(Enum):
    PHYSICAL = "Physical"
    LOGICAL = "Logical"
    OTHER = "Other"


class CapabilityType1Type(Enum):
    USED = "Used"
    UNUSED = "Unused"
    TOTAL = "Total"
    COMMITTED = "Committed"
    AVAILABLE = "Available"
    UNATTAINABLE = "Unattainable"
    OTHER = "Other"


@dataclass
class CauseType:
    pass


@dataclass
class CertificateOfAnalysisReferenceType:
    pass


class ClassPropertyTypeType(Enum):
    """Defines the type of the property. Defined types are.

    - ClassType: the property value is defined for the class and there is no value associated with an instance;
    - InstanceType: the property value of the class is undefined; and
    - DefaultType: the property value is defined for the class as the default instance value, but individual instances of the class may redefine specific values.
    """
    CLASS_TYPE = "ClassType"
    INSTANCE_TYPE = "InstanceType"
    DEFAULT_TYPE = "DefaultType"
    INVENTORY = "Inventory"
    MIXED = "Mixed"
    OTHER = "Other"


@dataclass
class ConfidenceFactorType:
    pass


@dataclass
class CorrectionType:
    pass


class DataType1Type(Enum):
    AMOUNT = "Amount"
    BINARY_OBJECT = "BinaryObject"
    CODE = "Code"
    DATE_TIME = "DateTime"
    IDENTIFIER = "Identifier"
    INDICATOR = "Indicator"
    MEASURE = "Measure"
    NUMERIC = "Numeric"
    QUANTITY = "Quantity"
    TEXT = "Text"
    STRING = "string"
    BYTE = "byte"
    UNSIGNED_BYTE = "unsignedByte"
    BINARY = "binary"
    INTEGER = "integer"
    POSITIVE_INTEGER = "positiveInteger"
    NEGATIVE_INTEGER = "negativeInteger"
    NON_NEGATIVE_INTEGER = "nonNegativeInteger"
    NON_POSITIVE_INTEGER = "nonPositiveInteger"
    INT = "int"
    UNSIGNED_INT = "unsignedInt"
    LONG = "long"
    UNSIGNED_LONG = "unsignedLong"
    SHORT = "short"
    UNSIGNED_SHORT = "unsignedShort"
    DECIMAL = "decimal"
    FLOAT = "float"
    DOUBLE = "double"
    BOOLEAN = "boolean"
    TIME = "time"
    TIME_INSTANT = "timeInstant"
    TIME_PERIOD = "timePeriod"
    DURATION = "duration"
    DATE = "date"
    DATE_TIME_1 = "dateTime"
    MONTH = "month"
    YEAR = "year"
    CENTURY = "century"
    RECURRING_DAY = "recurringDay"
    RECURRING_DATE = "recurringDate"
    RECURRING_DURATION = "recurringDuration"
    NAME = "Name"
    QNAME = "QName"
    NCNAME = "NCName"
    URI_REFERENCE = "uriReference"
    LANGUAGE = "language"
    ID = "ID"
    IDREF = "IDREF"
    IDREFS = "IDREFS"
    ENTITY = "ENTITY"
    ENTITIES = "ENTITIES"
    NOTATION = "NOTATION"
    NMTOKEN = "NMTOKEN"
    NMTOKENS = "NMTOKENS"
    ENUMERATION = "Enumeration"
    SVG = "SVG"
    OTHER = "Other"


class DefinitionTypeType(Enum):
    """Defines the type of the definition of a process segment, operations
    definition, or operations segment. Defined types are:

    -       Pattern: a segment or definition used as a template for other segments or definitions;
    -       Instance: a segment or definition that may be directly scheduled and tracked.
    """
    PATTERN = "Pattern"
    INSTANCE = "Instance"


class Dependency1Type(Enum):
    NOT_FOLLOW = "NotFollow"
    POSSIBLE_PARALLEL = "PossibleParallel"
    NOT_IN_PARALLEL = "NotInParallel"
    AT_START = "AtStart"
    AFTER_START = "AfterStart"
    AFTER_END = "AfterEnd"
    NO_LATER_AFTER_START = "NoLaterAfterStart"
    NO_EARLIER_AFTER_START = "NoEarlierAfterStart"
    NO_LATER_AFTER_END = "NoLaterAfterEnd"
    NO_EARLIER_AFTER_END = "NoEarlierAfterEnd"
    OTHER = "Other"


@dataclass
class DescriptionType:
    pass


class EquipmentElementLevel1Type(Enum):
    ENTERPRISE = "Enterprise"
    SITE = "Site"
    AREA = "Area"
    PROCESS_CELL = "ProcessCell"
    UNIT = "Unit"
    PRODUCTION_LINE = "ProductionLine"
    WORK_CELL = "WorkCell"
    PRODUCTION_UNIT = "ProductionUnit"
    STORAGE_ZONE = "StorageZone"
    STORAGE_UNIT = "StorageUnit"
    WORK_CENTER = "WorkCenter"
    WORK_UNIT = "WorkUnit"
    EQUIPMENT_MODULE = "EquipmentModule"
    CONTROL_MODULE = "ControlModule"
    OTHER = "Other"


@dataclass
class EquipmentUseType:
    pass


@dataclass
class EvaluatedPropertyReferenceType:
    test_specification_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    evaluated_property_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvaluatedPropertyID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )


class JobOrderCommand1Type(Enum):
    START = "Start"
    STOP = "Stop"
    HOLD = "Hold"
    RESTART = "Restart"
    ABORT = "Abort"
    RESET = "Reset"
    PAUSE = "Pause"
    RESUME = "Resume"
    OTHER = "Other"


@dataclass
class JobOrderCommandRuleType:
    pass


class JobOrderDispatchStatus1Type(Enum):
    WAITING = "Waiting"
    PENDING = "Pending"
    CANCELLED = "Cancelled"
    DISPATCHED = "Dispatched"
    READY = "Ready"
    RUNNING = "Running"
    COMPLETED = "Completed"
    ABORTED = "Aborted"
    HELD = "Held"
    SUSPENDED = "Suspended"
    CLOSED = "Closed"
    OTHER = "Other"


class MaterialUse1Type(Enum):
    CONSUMABLE = "Consumable"
    CONSUMED = "Consumed"
    PRODUCED = "Produced"
    BY_PRODUCT_PRODUCED = "By-product Produced"
    CO_PRODUCT_PRODUCED = "Co-product Produced"
    YIELD_PRODUCED = "Yield Produced"
    MATERIAL_CONSUMED = "Material Consumed"
    MATERIAL_PRODUCED = "Material Produced"
    DESTRUCTIVE_SAMPLE = "Destructive Sample"
    RETURNED_SAMPLE = "Returned Sample"
    RETAINED_SAMPLE = "Retained Sample"
    INVENTORIED = "Inventoried"
    OTHER = "Other"


class OperationsType1Type(Enum):
    PRODUCTION = "Production"
    MAINTENANCE = "Maintenance"
    QUALITY = "Quality"
    INVENTORY = "Inventory"
    MIXED = "Mixed"
    OTHER = "Other"


@dataclass
class OtherDependencyType:
    pass


@dataclass
class PersonNameType:
    pass


@dataclass
class PersonnelUseType:
    pass


@dataclass
class PhysicalAssetUseType:
    pass


@dataclass
class PriorityType:
    pass


@dataclass
class ProblemType:
    pass


@dataclass
class ProductProductionRuleType:
    pass


@dataclass
class ReasonType:
    pass


class RelationshipForm1Type(Enum):
    PERMANENT = "Permanent"
    TRANSIENT = "Transient"
    OTHER = "Other"


class RelationshipType1Type(Enum):
    LOGICAL = "Logical"
    PHYSICAL = "Physical"
    OTHER = "Other"


class RequestState1Type(Enum):
    FORECAST = "Forecast"
    RELEASED = "Released"
    CANCELLED = "Cancelled"
    READY = "Ready"
    RUNNING = "Running"
    COMPLETED = "Completed"
    ABORTED = "Aborted"
    HELD = "Held"
    PAUSED = "Paused"
    CLOSED = "Closed"
    OTHER = "Other"


@dataclass
class RequestedPriorityType:
    pass


class RequiredByRequestedSegmentResponse1Type(Enum):
    REQUIRED = "Required"
    OPTIONAL = "Optional"
    OTHER = "Other"


class ResourceLocationType1Type(Enum):
    OPERATIONAL_LOCATION = "Operational Location"
    EQUIPMENT = "Equipment"
    PHYSICAL_ASSET = "Physical Asset"
    DESCRIPTION = "Description"
    OTHER = "Other"


class ResourceReferenceType1Type(Enum):
    PERSONNEL = "Personnel"
    PERSONNEL_CLASS = "Personnel Class"
    EQUIPMENT = "Equipment"
    EQUIPMENT_CLASS = "Equipment Class"
    MATERIAL_CLASS = "Material Class"
    MATERIAL_DEFINITION = "Material Definition"
    MATERIAL_LOT = "Material Lot"
    MATERIAL_SUBLOT = "Material Sublot"
    PHYSICAL_ASSET = "Physical Asset"
    PHYSICAL_ASSET_CLASS = "Physical Asset Class"
    WORK_MASTER = "Work Master"
    PROCESS_SEGMENT = "Process Segment"
    OTHER = "Other"


@dataclass
class ResourcesType:
    """Indicates the type of the resource referenced. Defined values are.

    - Personnel
    - Personnel Class
    - Equipment
    - Equipment Class
    - Material Class
    - Material Definition
    - Material Lot
    - Material Sublot
    - Physical Asset
    - Physical Ssset Class
    - Work Master
    - Process Segment
    """


class ResponseState1Type(Enum):
    READY = "Ready"
    RUNNING = "Running"
    COMPLETED = "Completed"
    ABORTED = "Aborted"
    HOLDING = "Holding"
    PAUSED = "Paused"
    OTHER = "Other"


@dataclass
class SpatialDefinitionType:
    """The spatial definition provides a means of communicating zero-
    dimensional point, one-dimensional line, or two-dimensional shape or three-
    dimensional solid geospatial location data for planning/scheduling,
    actuals, resources, and analytics.

    Spatial definition identifies a value and the predefined coordinate
    reference system.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    srid: Optional[str] = field(
        default=None,
        metadata={
            "name": "SRID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    sridauthority: Optional[str] = field(
        default=None,
        metadata={
            "name": "SRIDAuthority",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class StatusType:
    pass


@dataclass
class StorageHierarchyScopeType:
    pass


class TransActionCodeEnumerationType(Enum):
    ADD = "Add"
    CHANGE = "Change"
    DELETE = "Delete"
    REPLACED = "Replaced"
    ACCEPTED = "Accepted"
    MODIFIED = "Modified"
    REJECTED = "Rejected"


class TransConfirmationCodeType(Enum):
    ALWAYS = "Always"
    NEVER = "Never"
    ON_ERROR = "OnError"


@dataclass
class TransGetType:
    expression: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Expression",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TransReceiverType:
    logical_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogicalID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    component_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComponentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


class TransResponseCodeType(Enum):
    ALWAYS = "Always"
    ON_ERROR = "OnError"


@dataclass
class TransSignatureType:
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
    qualifying_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "qualifyingAgencyID",
            "type": "Attribute",
        }
    )


@dataclass
class TransUserAreaType:
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class UnitOfMeasureType:
    pass


@dataclass
class VersionType:
    pass


class WorkType1Type(Enum):
    WORK_MASTER = "Work Master"
    WORK_DIRECTIVE = "Work Directive"
    OTHER = "Other"


@dataclass
class AssemblyRelationshipType:
    """Defines the type of the relationships. Defined types are.

    - Permanent: an assembly that is not intended to be split during the production process;
    - Transient: a temporary assembly using during production, such as a pallet of different materials or a batch kit.
    """
    value: Optional[AssemblyRelationship1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class AssemblyTypeType:
    """Defines the type of the assembly. Defined types are.

    - physical: the components of the assembly are physically connected or in the same area.
    - logical: the components of the assembly are not necessarily physically connected or in the same area.
    """
    value: Optional[AssemblyType1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class CapabilityTypeType:
    """Defines the type of capability. Defined values are.

    - Committed: capacity that is committed for future productive use;
    - Unattainable: capacity that is not attainable for future productive use given the equipment condition, equipment utilization, personnel availability or material availability;
    - Available: capacity that is available for additional future productive use;
    - Used: a historical value that defines the portion of the capacity with acceptable quality;
    - Unused: a historical value that defines the portion of the capacity that was not used or had unacceptable quality; and
    - Total: the sum of used and unused capability or the sum of available, unattainable and committed capability.
    """
    value: Optional[CapabilityType1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class DataTypeType:
    value: Optional[DataType1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class DependencyType:
    """Defines an execution dependency constraint of two elements. Defined
    values are (explained using dependency type between element A and element
    B)

    -       at start: start B at A start;
    -       after start: start B after A start;
    -       after end: start B after A end;
    -       not follow: B cannot follow A;
    -       possible parallel: B may run in parallel to A;
    -       not in parallel: B may not run in parallel to A;
    -       no later after start: start B no later than dependency factor after A start:
    -       no earlier after start: start B no earlier than dependency factor after A start;
    -       no later after end: start B no later than dependency factor after A end;
    -       no earlier after end: B no earlier than dependency factor after A end.
    """
    value: Optional[Dependency1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class EquipmentElementLevelType:
    """Defines the role based equipment hierarchy level as defined in ISA 95.
    Defined values are:

    - Enterprise
    - Site
    - Area
    - WorkCenter
    - WorkUnit
    - ProcessCell
    - Unit
    - ProductionLine
    - WorkCell
    - ProductionUnit
    - StorageZone
    - StorageUnit
    - EquipmentModule
    - Control Module
    """
    value: Optional[EquipmentElementLevel1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class JobOrderCommandType:
    """Defines the commands to a job order, as defined in ISA 95 and ISA 88.
    Defined values are:

    - Start
    - Stop
    - Hold
    - Restart
    - Abort
    - Reset
    - Pause
    - Resume
    """
    value: Optional[JobOrderCommand1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class JobOrderDispatchStatusType:
    """Defines the states to a job order, as defined in ISA 95 and ISA 88.
    Defined values are.

    - Waiting
    - Pending
    - Cancelled
    - Dispatched
    - Ready
    - Running
    - Completed
    - Aborted
    - Held
    - Suspended
    - Closed
    """
    value: Optional[JobOrderDispatchStatus1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class MaterialUseType:
    """Defines the expected use of the material class, material definition,
    material lot, or material sublot in the context of the operations segment.
    Defined values for production operations are.

    - Consumable, Consumed, Produced, By-product Produced, Co-product Produced, and Yield Produced.
    Defined values for maintenance operations are
    - Consumable, Material Consumed, and Material Produced.
    Defined values for quality test operations are
    - Consumable, Destructive Sample, Returned Sample, and Retained Sample.
    Defined values for inventory operations defined values are
    - Consumable, Material Consumed, Material Produced, and Inventoried.
    """
    value: Optional[MaterialUse1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class OperationsRecordEntryTemplateType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    information_object: Optional[str] = field(
        default=None,
        metadata={
            "name": "InformationObject",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    information_object_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InformationObjectID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    effective_timestamp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveTimestamp",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    record_timestamp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecordTimestamp",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    information_object_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "InformationObjectType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OperationsRecordSpecTemplateType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    information_object_type: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InformationObjectType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    information_object_type_multiplicity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InformationObjectTypeMultiplicity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    action: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Action",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    action_multiplicity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ActionMultiplicity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OperationsRecordTemplateType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    action: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Action",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    effective_timestamp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveTimestamp",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    record_timestamp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecordTimestamp",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OperationsTypeType:
    """Describes the category of the activity. Defined values are.

    - Production, Maintenance, Quality, Inventory, or Mixed.
    - Mixed” can be used when the activity covers several categories.
    """
    value: Optional[OperationsType1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class QuantityStringType(AnyGenericValueType):
    pass


@dataclass
class RelationshipFormType:
    value: Optional[RelationshipForm1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class RelationshipTypeType:
    value: Optional[RelationshipType1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class RequestStateType:
    """Indicates the state of an operations or work request. Defined values
    are.

    - Forecast
    - Released
    - Cancelled
    - Waiting
    - Ready
    - Running
    - Completed
    - Aborted
    - Held
    - Suspended
    - Closed
    """
    value: Optional[RequestState1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class RequiredByRequestedSegmentResponseType:
    """Indicates if a segment response assicated with a segment request is
    required. Defined values are.

    - Required
    - Optional
    """
    value: Optional[RequiredByRequestedSegmentResponse1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class ResourceLocationTypeType:
    """Indicates whether the storage location attribute refers to an
    operational location, equipment or physical asset object, or contains a
    description of the storage location. Mandatory where a storage location is
    specified. Defined values are.

    -       Operational Location:   storage location attribute references an operational location (OperationalLocationID);
    -       Equipment:                              storage location attribute references an equipment object (EquipmentID);
    -       Physical Asset:                 storage location attribute references a physical asset (PhysicalAssetID); and
    -       Description:                    storage location attribute contains a description of the storage location, such as a street address.
    """
    value: Optional[ResourceLocationType1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class ResourceReferenceTypeType:
    value: Optional[ResourceReferenceType1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class ResponseStateType:
    """Defines the states to a operations response. Defined values are.

    - Ready
    - Running
    - Completed
    - Aborted
    - Holding
    - Paused
    - Closed
    """
    value: Optional[ResponseState1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class TransExpressionType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    action_code: Optional[Union[TransActionCodeEnumerationType, str]] = field(
        default=None,
        metadata={
            "name": "actionCode",
            "type": "Attribute",
            "required": True,
        }
    )
    expression_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "expressionLanguage",
            "type": "Attribute",
        }
    )


@dataclass
class TransSenderType:
    logical_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogicalID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    component_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComponentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    task_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaskID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    confirmation_code: Optional[TransConfirmationCodeType] = field(
        default=None,
        metadata={
            "name": "ConfirmationCode",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    authorization_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthorizationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TransStateChangeType:
    from_state_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FromStateCode",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    to_state_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToStateCode",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    change_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeDateTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    user_area: Optional[TransUserAreaType] = field(
        default=None,
        metadata={
            "name": "UserArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class ValueStringType(AnyGenericValueType):
    pass


@dataclass
class WorkTypeType:
    value: Optional[WorkType1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherValue",
            "type": "Attribute",
        }
    )


@dataclass
class HierarchyScopeType:
    """The hierarchy scope identifies where the exchanged information fits
    within the role-based equipment hierarchy.

    It defines the scope of the exchanged information, such as a site or
    area for which the information is relevant. The hierarchy scope
    identifies the associated instance in the role-based equipment
    hierarchy.
    """
    equipment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    equipment_element_level: Optional[EquipmentElementLevelType] = field(
        default=None,
        metadata={
            "name": "EquipmentElementLevel",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_level: Optional[EquipmentElementLevelType] = field(
        default=None,
        metadata={
            "name": "EquipmentLevel",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional["HierarchyScopeType"] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class LocationType:
    equipment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    equipment_element_level: Optional[EquipmentElementLevelType] = field(
        default=None,
        metadata={
            "name": "EquipmentElementLevel",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    location: Optional["LocationType"] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class QuantityValueType:
    quantity_string: Optional[QuantityStringType] = field(
        default=None,
        metadata={
            "name": "QuantityString",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    data_type: Optional[DataTypeType] = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    unit_of_measure: Optional[UnitOfMeasureType] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasure",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class ResourceLocationType:
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    location_type: Optional[ResourceLocationTypeType] = field(
        default=None,
        metadata={
            "name": "LocationType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )


@dataclass
class ResultType:
    value_string: Optional[ValueStringType] = field(
        default=None,
        metadata={
            "name": "ValueString",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    data_type: Optional[DataTypeType] = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    unit_of_measure: Optional[UnitOfMeasureType] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasure",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TransApplicationAreaType:
    sender: Optional[TransSenderType] = field(
        default=None,
        metadata={
            "name": "Sender",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    receiver: List[TransReceiverType] = field(
        default_factory=list,
        metadata={
            "name": "Receiver",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    creation_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreationDateTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    signature: Optional[TransSignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    bodid: Optional[str] = field(
        default=None,
        metadata={
            "name": "BODID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    user_area: Optional[TransUserAreaType] = field(
        default=None,
        metadata={
            "name": "UserArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TransChangeStatusType:
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: Optional[DescriptionType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    effective_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDateTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    reason_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    reason: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    state_change: List[TransStateChangeType] = field(
        default_factory=list,
        metadata={
            "name": "StateChange",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    user_area: Optional[TransUserAreaType] = field(
        default=None,
        metadata={
            "name": "UserArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class ValueType:
    value_string: Optional[ValueStringType] = field(
        default=None,
        metadata={
            "name": "ValueString",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    data_type: Optional[DataTypeType] = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    unit_of_measure: Optional[UnitOfMeasureType] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasure",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class EquipmentAssetMappingType:
    equipment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    physical_asset_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhysicalAssetID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpEquipmentCapabilityPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_capability_property: List["OpEquipmentCapabilityPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentCapabilityProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpEquipmentRequirementPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_requirement_property: List["OpEquipmentRequirementPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentRequirementProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpEquipmentSpecificationPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_specification_property: List["OpEquipmentSpecificationPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentSpecificationProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpMaterialCapabilityPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    materal_capability_property: List["OpMaterialCapabilityPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "MateralCapabilityProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpMaterialRequirementPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_requirement_property: List["OpMaterialRequirementPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "MaterialRequirementProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpMaterialSpecificationPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_specification_property: List["OpMaterialSpecificationPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "MaterialSpecificationProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPersonnelCapabilityPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    personnel_capability_property: List["OpPersonnelCapabilityPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "PersonnelCapabilityProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPersonnelRequirementPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    personnel_requirement_property: List["OpPersonnelRequirementPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "PersonnelRequirementProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPersonnelSpecificationPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    personnel_specification_property: List["OpPersonnelSpecificationPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "PersonnelSpecificationProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPhysicalAssetCapabilityPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_capability_property: List["OpPhysicalAssetCapabilityPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetCapabilityProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPhysicalAssetRequirementPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_requirement_property: List["OpPhysicalAssetRequirementPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetRequirementProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPhysicalAssetSpecificationPropertyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_specification_property: List["OpPhysicalAssetSpecificationPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetSpecificationProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class ParameterType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    value: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    parameter: List["ParameterType"] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class SegmentDependencyType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    dependency: Optional[DependencyType] = field(
        default=None,
        metadata={
            "name": "Dependency",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    timing_factor: List[ValueType] = field(
        default_factory=list,
        metadata={
            "name": "TimingFactor",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    unit_of_measure: Optional[UnitOfMeasureType] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasure",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    product_segment_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ProductSegmentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "sequential": True,
        }
    )
    process_segment_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ProcessSegmentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "sequential": True,
        }
    )
    segment_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SegmentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "sequential": True,
        }
    )


@dataclass
class TestPropertyMeasurementType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    measurement_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "MeasurementDate",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    value: Optional[ValueType] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    expiration: Optional[str] = field(
        default=None,
        metadata={
            "name": "Expiration",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    work_definition_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorkDefinitionID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )


@dataclass
class TransActionCriteriaType:
    action_expression: List[TransExpressionType] = field(
        default_factory=list,
        metadata={
            "name": "ActionExpression",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    change_status: Optional[TransChangeStatusType] = field(
        default=None,
        metadata={
            "name": "ChangeStatus",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TransResponseCriteriaType:
    response_expression: Optional[TransExpressionType] = field(
        default=None,
        metadata={
            "name": "ResponseExpression",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    change_status: Optional[TransChangeStatusType] = field(
        default=None,
        metadata={
            "name": "ChangeStatus",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpEquipmentCapabilityType:
    equipment_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    capability_type: Optional[CapabilityTypeType] = field(
        default=None,
        metadata={
            "name": "CapabilityType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    reason: Optional[ReasonType] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    confidence_factor: Optional[ConfidenceFactorType] = field(
        default=None,
        metadata={
            "name": "ConfidenceFactor",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    operational_location: Optional[ResourceLocationType] = field(
        default=None,
        metadata={
            "name": "OperationalLocation",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_use: Optional[EquipmentUseType] = field(
        default=None,
        metadata={
            "name": "EquipmentUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_capability: List["OpEquipmentCapabilityType"] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentCapability",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_capability_property: List[OpEquipmentCapabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentCapabilityProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpEquipmentRequirementType:
    equipment_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_use: Optional[EquipmentUseType] = field(
        default=None,
        metadata={
            "name": "EquipmentUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    operational_location: Optional[ResourceLocationType] = field(
        default=None,
        metadata={
            "name": "OperationalLocation",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_level: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "EquipmentLevel",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_requirement_property: List[OpEquipmentRequirementPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentRequirementProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    required_by_requested_segment_response: Optional[RequiredByRequestedSegmentResponseType] = field(
        default=None,
        metadata={
            "name": "RequiredByRequestedSegmentResponse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpEquipmentSpecificationType:
    equipment_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_use: Optional[EquipmentUseType] = field(
        default=None,
        metadata={
            "name": "EquipmentUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_specification_property: List[OpEquipmentSpecificationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentSpecificationProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpMaterialCapabilityType:
    material_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_definition_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialDefinitionID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_lot_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialLotID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_sub_lot_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialSubLotID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    capability_type: Optional[CapabilityTypeType] = field(
        default=None,
        metadata={
            "name": "CapabilityType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    reason: Optional[ReasonType] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    confidence_factor: Optional[ConfidenceFactorType] = field(
        default=None,
        metadata={
            "name": "ConfidenceFactor",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_use: Optional[MaterialUseType] = field(
        default=None,
        metadata={
            "name": "MaterialUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    storage_location: Optional[ResourceLocationType] = field(
        default=None,
        metadata={
            "name": "StorageLocation",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_capability: List["OpMaterialCapabilityType"] = field(
        default_factory=list,
        metadata={
            "name": "AssemblyCapability",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_type: Optional[AssemblyTypeType] = field(
        default=None,
        metadata={
            "name": "AssemblyType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_relationship: Optional[AssemblyRelationshipType] = field(
        default=None,
        metadata={
            "name": "AssemblyRelationship",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_capability_property: List[OpMaterialCapabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialCapabilityProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpMaterialRequirementType:
    material_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_definition_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialDefinitionID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_lot_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialLotID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_sub_lot_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialSubLotID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_use: Optional[MaterialUseType] = field(
        default=None,
        metadata={
            "name": "MaterialUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    storage_location: Optional[ResourceLocationType] = field(
        default=None,
        metadata={
            "name": "StorageLocation",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_requirement: List["OpMaterialRequirementType"] = field(
        default_factory=list,
        metadata={
            "name": "AssemblyRequirement",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_type: Optional[AssemblyTypeType] = field(
        default=None,
        metadata={
            "name": "AssemblyType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_relationship: Optional[AssemblyRelationshipType] = field(
        default=None,
        metadata={
            "name": "AssemblyRelationship",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_requirement_property: List[OpMaterialRequirementPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialRequirementProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    required_by_requested_segment_response: Optional[RequiredByRequestedSegmentResponseType] = field(
        default=None,
        metadata={
            "name": "RequiredByRequestedSegmentResponse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpMaterialSpecificationType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    material_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_definition_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialDefinitionID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_use: Optional[MaterialUseType] = field(
        default=None,
        metadata={
            "name": "MaterialUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_specification: List["OpMaterialSpecificationType"] = field(
        default_factory=list,
        metadata={
            "name": "AssemblySpecification",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_type: Optional[AssemblyTypeType] = field(
        default=None,
        metadata={
            "name": "AssemblyType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_relationship: Optional[AssemblyRelationshipType] = field(
        default=None,
        metadata={
            "name": "AssemblyRelationship",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_specification_property: List[OpMaterialSpecificationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialSpecificationProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPersonnelCapabilityType:
    personnel_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PersonnelClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    person_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PersonID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    capability_type: Optional[CapabilityTypeType] = field(
        default=None,
        metadata={
            "name": "CapabilityType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    reason: Optional[ReasonType] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    confidence_factor: Optional[ConfidenceFactorType] = field(
        default=None,
        metadata={
            "name": "ConfidenceFactor",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    operational_location: Optional[ResourceLocationType] = field(
        default=None,
        metadata={
            "name": "OperationalLocation",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    personnel_use: Optional[PersonnelUseType] = field(
        default=None,
        metadata={
            "name": "PersonnelUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    personnel_capability: List["OpPersonnelCapabilityType"] = field(
        default_factory=list,
        metadata={
            "name": "PersonnelCapability",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    personnel_capability_property: List[OpPersonnelCapabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "PersonnelCapabilityProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPersonnelRequirementType:
    personnel_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PersonnelClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    person_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PersonID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    personnel_use: Optional[PersonnelUseType] = field(
        default=None,
        metadata={
            "name": "PersonnelUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    operational_location: Optional[ResourceLocationType] = field(
        default=None,
        metadata={
            "name": "OperationalLocation",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    personnel_requirement_property: List[OpPersonnelRequirementPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "PersonnelRequirementProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    required_by_requested_segment_response: Optional[RequiredByRequestedSegmentResponseType] = field(
        default=None,
        metadata={
            "name": "RequiredByRequestedSegmentResponse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPersonnelSpecificationType:
    personnel_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PersonnelClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    person_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PersonID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    personnel_use: Optional[PersonnelUseType] = field(
        default=None,
        metadata={
            "name": "PersonnelUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    personnel_specification_property: List[OpPersonnelSpecificationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "PersonnelSpecificationProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPhysicalAssetCapabilityType:
    physical_asset_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    capability_type: Optional[CapabilityTypeType] = field(
        default=None,
        metadata={
            "name": "CapabilityType",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    reason: Optional[ReasonType] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    confidence_factor: Optional[ConfidenceFactorType] = field(
        default=None,
        metadata={
            "name": "ConfidenceFactor",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_location: Optional[ResourceLocationType] = field(
        default=None,
        metadata={
            "name": "PhysicalLocation",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_use: Optional[PhysicalAssetUseType] = field(
        default=None,
        metadata={
            "name": "PhysicalAssetUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_capability: List["OpPhysicalAssetCapabilityType"] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetCapability",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_capability_property: List[OpPhysicalAssetCapabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetCapabilityProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPhysicalAssetRequirementType:
    physical_asset_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_use: Optional[PhysicalAssetUseType] = field(
        default=None,
        metadata={
            "name": "PhysicalAssetUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_location: Optional[ResourceLocationType] = field(
        default=None,
        metadata={
            "name": "PhysicalLocation",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_level: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "EquipmentLevel",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_requirement_property: List[OpPhysicalAssetRequirementPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetRequirementProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    required_by_requested_segment_response: Optional[RequiredByRequestedSegmentResponseType] = field(
        default=None,
        metadata={
            "name": "RequiredByRequestedSegmentResponse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class OpPhysicalAssetSpecificationType:
    physical_asset_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_use: Optional[PhysicalAssetUseType] = field(
        default=None,
        metadata={
            "name": "PhysicalAssetUse",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    quantity: List[QuantityValueType] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_specification_property: List[OpPhysicalAssetSpecificationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetSpecificationProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TestResultType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    evaluation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvaluationDate",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    evaluated_criterion_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvaluatedCriterionResult",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    expiration: Optional[str] = field(
        default=None,
        metadata={
            "name": "Expiration",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    test_result: List["TestResultType"] = field(
        default_factory=list,
        metadata={
            "name": "TestResult",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    property_measurement: List[TestPropertyMeasurementType] = field(
        default_factory=list,
        metadata={
            "name": "PropertyMeasurement",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )


@dataclass
class TransAcknowledgeType:
    original_application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "OriginalApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    response_criteria: List[TransResponseCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "ResponseCriteria",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TransCancelType:
    action_criteria: List[TransActionCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "ActionCriteria",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TransChangeType:
    action_criteria: List[TransActionCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "ActionCriteria",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    response_code: Optional[TransResponseCodeType] = field(
        default=None,
        metadata={
            "name": "responseCode",
            "type": "Attribute",
        }
    )


@dataclass
class TransConfirmType:
    original_application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "OriginalApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    response_criteria: List[TransResponseCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "ResponseCriteria",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TransProcessType:
    action_criteria: List[TransActionCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "ActionCriteria",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    acknowledge_code: Optional[TransResponseCodeType] = field(
        default=None,
        metadata={
            "name": "acknowledgeCode",
            "type": "Attribute",
        }
    )


@dataclass
class TransRespondType:
    original_application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "OriginalApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    response_criteria: List[TransResponseCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "ResponseCriteria",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TransShowType:
    original_application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "OriginalApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    response_criteria: List[TransResponseCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "ResponseCriteria",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TransSyncType:
    action_criteria: List[TransActionCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "ActionCriteria",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )

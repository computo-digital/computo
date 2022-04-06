from dataclasses import dataclass, field
from typing import List, Optional
from generated.b2_mml_common import (
    ClassPropertyTypeType,
    DescriptionType,
    EquipmentAssetMappingType,
    EvaluatedPropertyReferenceType,
    HierarchyScopeType,
    ResourceLocationType,
    SpatialDefinitionType,
    TestResultType,
    TransAcknowledgeType,
    TransApplicationAreaType,
    TransCancelType,
    TransChangeType,
    TransGetType,
    TransProcessType,
    TransRespondType,
    TransShowType,
    TransSyncType,
    ValueType,
)
from generated.b2_mml_test_specification import TestSpecificationType

__NAMESPACE__ = "http://www.mesa.org/xml/B2MML"


@dataclass
class EquipmentClassPropertyType:
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
    property_type: Optional[ClassPropertyTypeType] = field(
        default=None,
        metadata={
            "name": "PropertyType",
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
    equipment_class_property: List["EquipmentClassPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentClassProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    evaluated_property_reference: List[EvaluatedPropertyReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "EvaluatedPropertyReference",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class EquipmentPropertyType:
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
    equipment_property: List["EquipmentPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    evaluated_property_reference: List[EvaluatedPropertyReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "EvaluatedPropertyReference",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_result: List[TestResultType] = field(
        default_factory=list,
        metadata={
            "name": "TestResult",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class EquipmentClassType:
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
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
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
    equipment_class_property: List[EquipmentClassPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentClassProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_class: List["EquipmentClassType"] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentClass",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    uses_properties_of_equipment_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "UsesPropertiesOfEquipmentClassID",
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
    equipment_capability_test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentCapabilityTestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class EquipmentType:
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
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
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
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_asset_mapping: List[EquipmentAssetMappingType] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentAssetMapping",
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
    equipment_property: List[EquipmentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment: List["EquipmentType"] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_capability_test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentCapabilityTestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class AcknowledgeEquipmentClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgeEquipmentClassType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        acknowledge: Optional[TransAcknowledgeType] = field(
            default=None,
            metadata={
                "name": "Acknowledge",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_class: List[EquipmentClassType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgeEquipmentType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgeEquipmentType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        acknowledge: Optional[TransAcknowledgeType] = field(
            default=None,
            metadata={
                "name": "Acknowledge",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment: List[EquipmentType] = field(
            default_factory=list,
            metadata={
                "name": "Equipment",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelEquipmentClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelEquipmentClassType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        cancel: Optional[TransCancelType] = field(
            default=None,
            metadata={
                "name": "Cancel",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_class: List[EquipmentClassType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelEquipmentType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelEquipmentType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        cancel: Optional[TransCancelType] = field(
            default=None,
            metadata={
                "name": "Cancel",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment: List[EquipmentType] = field(
            default_factory=list,
            metadata={
                "name": "Equipment",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangeEquipmentClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangeEquipmentClassType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        change: Optional[TransChangeType] = field(
            default=None,
            metadata={
                "name": "Change",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_class: List[EquipmentClassType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangeEquipmentType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangeEquipmentType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        change: Optional[TransChangeType] = field(
            default=None,
            metadata={
                "name": "Change",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment: List[EquipmentType] = field(
            default_factory=list,
            metadata={
                "name": "Equipment",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class Equipment(EquipmentType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class EquipmentClass(EquipmentClassType):
    """A representation of a grouping of equipment with similar characteristics
    for a definite purpose such as manufacturing operations definition,
    scheduling, capability and performance is an equipment class.

    Any piece of equipment may be a member of zero or more equipment
    classes. An equipment class may be defined as a specialization of
    zero or more equipment classes. An equipment class may be made up of
    zero or more equipment classes.
    """
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class EquipmentInformationType:
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
    hierarchy_scope: Optional[HierarchyScopeType] = field(
        default=None,
        metadata={
            "name": "HierarchyScope",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    published_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublishedDate",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment: List[EquipmentType] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_class: List[EquipmentClassType] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentClass",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    equipment_capability_test_specification: List[TestSpecificationType] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentCapabilityTestSpecification",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class GetEquipmentClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetEquipmentClassType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        get: Optional[TransGetType] = field(
            default=None,
            metadata={
                "name": "Get",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_class: List[EquipmentClassType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetEquipmentType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetEquipmentType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        get: Optional[TransGetType] = field(
            default=None,
            metadata={
                "name": "Get",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment: List[EquipmentType] = field(
            default_factory=list,
            metadata={
                "name": "Equipment",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessEquipmentClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessEquipmentClassType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        process: Optional[TransProcessType] = field(
            default=None,
            metadata={
                "name": "Process",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_class: List[EquipmentClassType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessEquipmentType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessEquipmentType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        process: Optional[TransProcessType] = field(
            default=None,
            metadata={
                "name": "Process",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment: List[EquipmentType] = field(
            default_factory=list,
            metadata={
                "name": "Equipment",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondEquipmentClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondEquipmentClassType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        respond: Optional[TransRespondType] = field(
            default=None,
            metadata={
                "name": "Respond",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_class: List[EquipmentClassType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondEquipmentType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondEquipmentType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        respond: Optional[TransRespondType] = field(
            default=None,
            metadata={
                "name": "Respond",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment: List[EquipmentType] = field(
            default_factory=list,
            metadata={
                "name": "Equipment",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowEquipmentClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowEquipmentClassType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        show: Optional[TransShowType] = field(
            default=None,
            metadata={
                "name": "Show",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_class: List[EquipmentClassType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowEquipmentType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowEquipmentType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        show: Optional[TransShowType] = field(
            default=None,
            metadata={
                "name": "Show",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment: List[EquipmentType] = field(
            default_factory=list,
            metadata={
                "name": "Equipment",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncEquipmentClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncEquipmentClassType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        sync: Optional[TransSyncType] = field(
            default=None,
            metadata={
                "name": "Sync",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_class: List[EquipmentClassType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncEquipmentType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncEquipmentType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        sync: Optional[TransSyncType] = field(
            default=None,
            metadata={
                "name": "Sync",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment: List[EquipmentType] = field(
            default_factory=list,
            metadata={
                "name": "Equipment",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgeEquipment(AcknowledgeEquipmentType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class AcknowledgeEquipmentClass(AcknowledgeEquipmentClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class AcknowledgeEquipmentInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgeEquipmentInformationType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        acknowledge: Optional[TransAcknowledgeType] = field(
            default=None,
            metadata={
                "name": "Acknowledge",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_information: List[EquipmentInformationType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelEquipment(CancelEquipmentType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelEquipmentClass(CancelEquipmentClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelEquipmentInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelEquipmentInformationType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        cancel: Optional[TransCancelType] = field(
            default=None,
            metadata={
                "name": "Cancel",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_information: List[EquipmentInformationType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangeEquipment(ChangeEquipmentType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangeEquipmentClass(ChangeEquipmentClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangeEquipmentInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangeEquipmentInformationType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        change: Optional[TransChangeType] = field(
            default=None,
            metadata={
                "name": "Change",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_information: List[EquipmentInformationType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class EquipmentInformation(EquipmentInformationType):
    """
    A collection of Role Based Equipment Class and Equipment instance
    definitions.
    """
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetEquipment(GetEquipmentType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetEquipmentClass(GetEquipmentClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetEquipmentInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetEquipmentInformationType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        get: Optional[TransGetType] = field(
            default=None,
            metadata={
                "name": "Get",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_information: List[EquipmentInformationType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessEquipment(ProcessEquipmentType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessEquipmentClass(ProcessEquipmentClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessEquipmentInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessEquipmentInformationType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        process: Optional[TransProcessType] = field(
            default=None,
            metadata={
                "name": "Process",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_information: List[EquipmentInformationType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondEquipment(RespondEquipmentType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondEquipmentClass(RespondEquipmentClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondEquipmentInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondEquipmentInformationType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        respond: Optional[TransRespondType] = field(
            default=None,
            metadata={
                "name": "Respond",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_information: List[EquipmentInformationType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowEquipment(ShowEquipmentType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowEquipmentClass(ShowEquipmentClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowEquipmentInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowEquipmentInformationType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        show: Optional[TransShowType] = field(
            default=None,
            metadata={
                "name": "Show",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_information: List[EquipmentInformationType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncEquipment(SyncEquipmentType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncEquipmentClass(SyncEquipmentClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncEquipmentInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncEquipmentInformationType.DataArea"] = field(
        default=None,
        metadata={
            "name": "DataArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseID",
            "type": "Attribute",
            "required": True,
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionID",
            "type": "Attribute",
        }
    )

    @dataclass
    class DataArea:
        sync: Optional[TransSyncType] = field(
            default=None,
            metadata={
                "name": "Sync",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "required": True,
            }
        )
        equipment_information: List[EquipmentInformationType] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgeEquipmentInformation(AcknowledgeEquipmentInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelEquipmentInformation(CancelEquipmentInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangeEquipmentInformation(ChangeEquipmentInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetEquipmentInformation(GetEquipmentInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessEquipmentInformation(ProcessEquipmentInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondEquipmentInformation(RespondEquipmentInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowEquipmentInformation(ShowEquipmentInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncEquipmentInformation(SyncEquipmentInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"

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
class PhysicalAssetClassPropertyType:
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
    physical_asset_class_property: List["PhysicalAssetClassPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetClassProperty",
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
class PhysicalAssetPropertyType:
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
    physical_asset_property: List["PhysicalAssetPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetProperty",
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
class PhysicalAssetClassType:
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
    manufacturer: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_class: List["PhysicalAssetClassType"] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetClass",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    uses_properties_of_physical_asset_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "UsesPropertiesOfPhysicalAssetClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_class_property: List[PhysicalAssetClassPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetClassProperty",
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
    physical_asset_capability_test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetCapabilityTestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class PhysicalAssetType:
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
    fixed_asset_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FixedAssetID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    vendor_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorID",
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
    equipment_asset_mapping: List[EquipmentAssetMappingType] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentAssetMapping",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_property: List[PhysicalAssetPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset: List["PhysicalAssetType"] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAsset",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_capability_test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetCapabilityTestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class AcknowledgePhysicalAssetClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgePhysicalAssetClassType.DataArea"] = field(
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
        physical_asset_class: List[PhysicalAssetClassType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgePhysicalAssetType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgePhysicalAssetType.DataArea"] = field(
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
        physical_asset: List[PhysicalAssetType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAsset",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelPhysicalAssetClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelPhysicalAssetClassType.DataArea"] = field(
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
        physical_asset_class: List[PhysicalAssetClassType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelPhysicalAssetType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelPhysicalAssetType.DataArea"] = field(
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
        physical_asset: List[PhysicalAssetType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAsset",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangePhysicalAssetClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangePhysicalAssetClassType.DataArea"] = field(
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
        physical_asset_class: List[PhysicalAssetClassType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangePhysicalAssetType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangePhysicalAssetType.DataArea"] = field(
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
        physical_asset: List[PhysicalAssetType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAsset",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetPhysicalAssetClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetPhysicalAssetClassType.DataArea"] = field(
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
        physical_asset_class: List[PhysicalAssetClassType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetPhysicalAssetType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetPhysicalAssetType.DataArea"] = field(
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
        physical_asset: List[PhysicalAssetType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAsset",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class PhysicalAsset(PhysicalAssetType):
    """
    A representation of a physical piece of equipment is a physical asset.
    """
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class PhysicalAssetClass(PhysicalAssetClassType):
    """A representation of a grouping of physical assets with similar
    characteristics for purposes of repair and replacement is a physical asset
    class.

    Any physical asset is a member of one physical asset class. A
    physical asset class may be defined as a specialization of zero or
    more physical asset classes. A physical asset class may be made up
    of zero or more physical asset classes.
    """
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class PhysicalAssetInformationType:
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
    physical_asset: List[PhysicalAssetType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAsset",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_class: List[PhysicalAssetClassType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetClass",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_asset_capability_test_specification: List[TestSpecificationType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAssetCapabilityTestSpecification",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class ProcessPhysicalAssetClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessPhysicalAssetClassType.DataArea"] = field(
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
        physical_asset_class: List[PhysicalAssetClassType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessPhysicalAssetType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessPhysicalAssetType.DataArea"] = field(
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
        physical_asset: List[PhysicalAssetType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAsset",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondPhysicalAssetClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondPhysicalAssetClassType.DataArea"] = field(
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
        physical_asset_class: List[PhysicalAssetClassType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondPhysicalAssetType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondPhysicalAssetType.DataArea"] = field(
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
        physical_asset: List[PhysicalAssetType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAsset",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowPhysicalAssetClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowPhysicalAssetClassType.DataArea"] = field(
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
        physical_asset_class: List[PhysicalAssetClassType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowPhysicalAssetType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowPhysicalAssetType.DataArea"] = field(
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
        physical_asset: List[PhysicalAssetType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAsset",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncPhysicalAssetClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncPhysicalAssetClassType.DataArea"] = field(
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
        physical_asset_class: List[PhysicalAssetClassType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncPhysicalAssetType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncPhysicalAssetType.DataArea"] = field(
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
        physical_asset: List[PhysicalAssetType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAsset",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgePhysicalAsset(AcknowledgePhysicalAssetType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class AcknowledgePhysicalAssetClass(AcknowledgePhysicalAssetClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class AcknowledgePhysicalAssetInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgePhysicalAssetInformationType.DataArea"] = field(
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
        physical_asset_information: List[PhysicalAssetInformationType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelPhysicalAsset(CancelPhysicalAssetType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelPhysicalAssetClass(CancelPhysicalAssetClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelPhysicalAssetInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelPhysicalAssetInformationType.DataArea"] = field(
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
        physical_asset_information: List[PhysicalAssetInformationType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangePhysicalAsset(ChangePhysicalAssetType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangePhysicalAssetClass(ChangePhysicalAssetClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangePhysicalAssetInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangePhysicalAssetInformationType.DataArea"] = field(
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
        physical_asset_information: List[PhysicalAssetInformationType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetPhysicalAsset(GetPhysicalAssetType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetPhysicalAssetClass(GetPhysicalAssetClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetPhysicalAssetInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetPhysicalAssetInformationType.DataArea"] = field(
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
        physical_asset_information: List[PhysicalAssetInformationType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class PhysicalAssetInformation(PhysicalAssetInformationType):
    """The physical asset model contains information about the physical piece
    of equipment, usually managed as a physical asset within the enterprise
    often utilizing a specific serial number.

    An object in the equipment model defines a role for the equipment,
    and object in the physical asset model defines the physical asset ID
    and properties of a piece of equipment.
    """
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessPhysicalAsset(ProcessPhysicalAssetType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessPhysicalAssetClass(ProcessPhysicalAssetClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessPhysicalAssetInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessPhysicalAssetInformationType.DataArea"] = field(
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
        physical_asset_information: List[PhysicalAssetInformationType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondPhysicalAsset(RespondPhysicalAssetType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondPhysicalAssetClass(RespondPhysicalAssetClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondPhysicalAssetInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondPhysicalAssetInformationType.DataArea"] = field(
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
        physical_asset_information: List[PhysicalAssetInformationType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowPhysicalAsset(ShowPhysicalAssetType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowPhysicalAssetClass(ShowPhysicalAssetClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowPhysicalAssetInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowPhysicalAssetInformationType.DataArea"] = field(
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
        physical_asset_information: List[PhysicalAssetInformationType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncPhysicalAsset(SyncPhysicalAssetType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncPhysicalAssetClass(SyncPhysicalAssetClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncPhysicalAssetInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncPhysicalAssetInformationType.DataArea"] = field(
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
        physical_asset_information: List[PhysicalAssetInformationType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalAssetInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgePhysicalAssetInformation(AcknowledgePhysicalAssetInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelPhysicalAssetInformation(CancelPhysicalAssetInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangePhysicalAssetInformation(ChangePhysicalAssetInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetPhysicalAssetInformation(GetPhysicalAssetInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessPhysicalAssetInformation(ProcessPhysicalAssetInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondPhysicalAssetInformation(RespondPhysicalAssetInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowPhysicalAssetInformation(ShowPhysicalAssetInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncPhysicalAssetInformation(SyncPhysicalAssetInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"

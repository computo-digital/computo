from dataclasses import dataclass, field
from typing import List, Optional
from generated.b2_mml_common import (
    AssemblyRelationshipType,
    AssemblyTypeType,
    ClassPropertyTypeType,
    DescriptionType,
    EvaluatedPropertyReferenceType,
    HierarchyScopeType,
    QuantityValueType,
    SpatialDefinitionType,
    StatusType,
    StorageHierarchyScopeType,
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
class MaterialClassPropertyType:
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
    material_class_property: List["MaterialClassPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "MaterialClassProperty",
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
class MaterialDefinitionPropertyType:
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
    material_definition_property: List["MaterialDefinitionPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "MaterialDefinitionProperty",
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
class MaterialLotPropertyType:
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
    material_lot_property: List["MaterialLotPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "MaterialLotProperty",
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
class MaterialClassType:
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
    uses_properties_of_material_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "UsesPropertiesOfMaterialClassID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_class_property: List[MaterialClassPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialClassProperty",
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
    material_test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialTestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_class_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AssemblyClassID",
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


@dataclass
class MaterialDefinitionType:
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
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_definition_property: List[MaterialDefinitionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialDefinitionProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
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
    material_lot_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialLotID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialTestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_definition_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AssemblyDefinitionID",
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


@dataclass
class MaterialSubLotType:
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
    status: Optional[StatusType] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_sublot_property: List[MaterialLotPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialSublotProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    storage_location: Optional[StorageHierarchyScopeType] = field(
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
    material_sub_lot: List["MaterialSubLotType"] = field(
        default_factory=list,
        metadata={
            "name": "MaterialSubLot",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_lot_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaterialLotID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_lot_id: List["MaterialLotType"] = field(
        default_factory=list,
        metadata={
            "name": "AssemblyLotID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_sub_lot_id: List["MaterialSubLotType"] = field(
        default_factory=list,
        metadata={
            "name": "AssemblySubLotID",
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


@dataclass
class AcknowledgeMaterialClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgeMaterialClassType.DataArea"] = field(
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
        material_class: List[MaterialClassType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgeMaterialDefinitionType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgeMaterialDefinitionType.DataArea"] = field(
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
        material_definition: List[MaterialDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialDefinition",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgeMaterialSubLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgeMaterialSubLotType.DataArea"] = field(
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
        material_sub_lot: List[MaterialSubLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialSubLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelMaterialClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelMaterialClassType.DataArea"] = field(
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
        material_class: List[MaterialClassType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelMaterialDefinitionType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelMaterialDefinitionType.DataArea"] = field(
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
        material_definition: List[MaterialDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialDefinition",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelMaterialSubLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelMaterialSubLotType.DataArea"] = field(
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
        material_sub_lot: List[MaterialSubLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialSubLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangeMaterialClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangeMaterialClassType.DataArea"] = field(
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
        material_class: List[MaterialClassType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangeMaterialDefinitionType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangeMaterialDefinitionType.DataArea"] = field(
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
        material_definition: List[MaterialDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialDefinition",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangeMaterialSubLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangeMaterialSubLotType.DataArea"] = field(
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
        material_sub_lot: List[MaterialSubLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialSubLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetMaterialClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetMaterialClassType.DataArea"] = field(
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
        material_class: List[MaterialClassType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetMaterialDefinitionType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetMaterialDefinitionType.DataArea"] = field(
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
        material_definition: List[MaterialDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialDefinition",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetMaterialSubLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetMaterialSubLotType.DataArea"] = field(
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
        material_sub_lot: List[MaterialSubLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialSubLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class MaterialClass(MaterialClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class MaterialDefinition(MaterialDefinitionType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class MaterialLotType:
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
    spatial_definition: Optional[SpatialDefinitionType] = field(
        default=None,
        metadata={
            "name": "SpatialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_definition_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaterialDefinitionID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    status: Optional[StatusType] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_lot_property: List[MaterialLotPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialLotProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    material_sub_lot: List[MaterialSubLotType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialSubLot",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    storage_location: Optional[StorageHierarchyScopeType] = field(
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
    material_test_specification_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaterialTestSpecificationID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_lot_id: List["MaterialLotType"] = field(
        default_factory=list,
        metadata={
            "name": "AssemblyLotID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    assembly_sub_lot_id: List[MaterialSubLotType] = field(
        default_factory=list,
        metadata={
            "name": "AssemblySubLotID",
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


@dataclass
class MaterialSubLot(MaterialSubLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessMaterialClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessMaterialClassType.DataArea"] = field(
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
        material_class: List[MaterialClassType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessMaterialDefinitionType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessMaterialDefinitionType.DataArea"] = field(
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
        material_definition: List[MaterialDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialDefinition",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessMaterialSubLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessMaterialSubLotType.DataArea"] = field(
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
        material_sub_lot: List[MaterialSubLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialSubLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondMaterialClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondMaterialClassType.DataArea"] = field(
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
        material_class: List[MaterialClassType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondMaterialDefinitionType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondMaterialDefinitionType.DataArea"] = field(
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
        material_definition: List[MaterialDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialDefinition",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondMaterialSubLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondMaterialSubLotType.DataArea"] = field(
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
        material_sub_lot: List[MaterialSubLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialSubLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowMaterialClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowMaterialClassType.DataArea"] = field(
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
        material_class: List[MaterialClassType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowMaterialDefinitionType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowMaterialDefinitionType.DataArea"] = field(
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
        material_definition: List[MaterialDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialDefinition",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowMaterialSubLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowMaterialSubLotType.DataArea"] = field(
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
        material_sub_lot: List[MaterialSubLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialSubLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncMaterialClassType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncMaterialClassType.DataArea"] = field(
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
        material_class: List[MaterialClassType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialClass",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncMaterialDefinitionType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncMaterialDefinitionType.DataArea"] = field(
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
        material_definition: List[MaterialDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialDefinition",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncMaterialSubLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncMaterialSubLotType.DataArea"] = field(
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
        material_sub_lot: List[MaterialSubLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialSubLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgeMaterialClass(AcknowledgeMaterialClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class AcknowledgeMaterialDefinition(AcknowledgeMaterialDefinitionType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class AcknowledgeMaterialLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgeMaterialLotType.DataArea"] = field(
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
        material_lot: List[MaterialLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgeMaterialSubLot(AcknowledgeMaterialSubLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelMaterialClass(CancelMaterialClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelMaterialDefinition(CancelMaterialDefinitionType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelMaterialLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelMaterialLotType.DataArea"] = field(
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
        material_lot: List[MaterialLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelMaterialSubLot(CancelMaterialSubLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangeMaterialClass(ChangeMaterialClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangeMaterialDefinition(ChangeMaterialDefinitionType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangeMaterialLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangeMaterialLotType.DataArea"] = field(
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
        material_lot: List[MaterialLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangeMaterialSubLot(ChangeMaterialSubLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetMaterialClass(GetMaterialClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetMaterialDefinition(GetMaterialDefinitionType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetMaterialLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetMaterialLotType.DataArea"] = field(
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
        material_lot: List[MaterialLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetMaterialSubLot(GetMaterialSubLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class MaterialInformationType:
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
    published_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublishedDate",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    material_class: List[MaterialClassType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialClass",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    material_definition: List[MaterialDefinitionType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialDefinition",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    material_lot: List[MaterialLotType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialLot",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    material_sub_lot: List[MaterialSubLotType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialSubLot",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )
    material_test_specification: List[TestSpecificationType] = field(
        default_factory=list,
        metadata={
            "name": "MaterialTestSpecification",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )


@dataclass
class MaterialLot(MaterialLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessMaterialClass(ProcessMaterialClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessMaterialDefinition(ProcessMaterialDefinitionType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessMaterialLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessMaterialLotType.DataArea"] = field(
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
        material_lot: List[MaterialLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessMaterialSubLot(ProcessMaterialSubLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondMaterialClass(RespondMaterialClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondMaterialDefinition(RespondMaterialDefinitionType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondMaterialLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondMaterialLotType.DataArea"] = field(
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
        material_lot: List[MaterialLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondMaterialSubLot(RespondMaterialSubLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowMaterialClass(ShowMaterialClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowMaterialDefinition(ShowMaterialDefinitionType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowMaterialLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowMaterialLotType.DataArea"] = field(
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
        material_lot: List[MaterialLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowMaterialSubLot(ShowMaterialSubLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncMaterialClass(SyncMaterialClassType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncMaterialDefinition(SyncMaterialDefinitionType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncMaterialLotType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncMaterialLotType.DataArea"] = field(
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
        material_lot: List[MaterialLotType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialLot",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncMaterialSubLot(SyncMaterialSubLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class AcknowledgeMaterialInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgeMaterialInformationType.DataArea"] = field(
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
        material_information: List[MaterialInformationType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class AcknowledgeMaterialLot(AcknowledgeMaterialLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelMaterialInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelMaterialInformationType.DataArea"] = field(
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
        material_information: List[MaterialInformationType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelMaterialLot(CancelMaterialLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangeMaterialInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangeMaterialInformationType.DataArea"] = field(
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
        material_information: List[MaterialInformationType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangeMaterialLot(ChangeMaterialLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetMaterialInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetMaterialInformationType.DataArea"] = field(
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
        material_information: List[MaterialInformationType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetMaterialLot(GetMaterialLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class MaterialInformation(MaterialInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessMaterialInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessMaterialInformationType.DataArea"] = field(
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
        material_information: List[MaterialInformationType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessMaterialLot(ProcessMaterialLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondMaterialInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondMaterialInformationType.DataArea"] = field(
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
        material_information: List[MaterialInformationType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondMaterialLot(RespondMaterialLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowMaterialInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowMaterialInformationType.DataArea"] = field(
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
        material_information: List[MaterialInformationType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowMaterialLot(ShowMaterialLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncMaterialInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncMaterialInformationType.DataArea"] = field(
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
        material_information: List[MaterialInformationType] = field(
            default_factory=list,
            metadata={
                "name": "MaterialInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncMaterialLot(SyncMaterialLotType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class AcknowledgeMaterialInformation(AcknowledgeMaterialInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelMaterialInformation(CancelMaterialInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangeMaterialInformation(ChangeMaterialInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetMaterialInformation(GetMaterialInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessMaterialInformation(ProcessMaterialInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondMaterialInformation(RespondMaterialInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowMaterialInformation(ShowMaterialInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncMaterialInformation(SyncMaterialInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"

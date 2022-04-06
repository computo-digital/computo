from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from generated.b2_mml_common import (
    DescriptionType,
    HierarchyScopeType,
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
    VersionType,
)

__NAMESPACE__ = "http://www.mesa.org/xml/B2MML"


@dataclass
class TestSpecificationCriteriaType:
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
    sequence: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Sequence",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    expression: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Expression",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    result: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Result",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    evaluated_property_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EvaluatedPropertyID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TestSpecificationEvaluatedPropertyType:
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
    test_specification_criteria_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationCriteriaID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    work_definition_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "WorkDefinitionID",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TestSpecificationPropertyType:
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
    test_specification_property: List["TestSpecificationPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class TestSpecificationType:
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
    version: Optional[VersionType] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    effective_start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveStartDate",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    effective_end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveEndDate",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    published_end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublishedEndDate",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_sample_size: Optional[ValueType] = field(
        default=None,
        metadata={
            "name": "TestSampleSize",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    recurrence_quantity: Optional[ValueType] = field(
        default=None,
        metadata={
            "name": "RecurrenceQuantity",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    recurrence_time_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RecurrenceTimeInterval",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    physical_sample_required: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhysicalSampleRequired",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification: List["TestSpecificationType"] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecification",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification_property: List[TestSpecificationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    test_specification_criteria: List[TestSpecificationCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecificationCriteria",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )
    evaluated_property: List[TestSpecificationEvaluatedPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "EvaluatedProperty",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
        }
    )


@dataclass
class AcknowledgeTestSpecificationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgeTestSpecificationType.DataArea"] = field(
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
        test_specification: List[TestSpecificationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecification",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelTestSpecificationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelTestSpecificationType.DataArea"] = field(
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
        test_specification: List[TestSpecificationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecification",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangeTestSpecificationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangeTestSpecificationType.DataArea"] = field(
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
        test_specification: List[TestSpecificationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecification",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetTestSpecificationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetTestSpecificationType.DataArea"] = field(
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
        test_specification: List[TestSpecificationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecification",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessTestSpecificationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessTestSpecificationType.DataArea"] = field(
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
        test_specification: List[TestSpecificationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecification",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondTestSpecificationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondTestSpecificationType.DataArea"] = field(
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
        test_specification: List[TestSpecificationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecification",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowTestSpecificationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowTestSpecificationType.DataArea"] = field(
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
        test_specification: List[TestSpecificationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecification",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncTestSpecificationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncTestSpecificationType.DataArea"] = field(
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
        test_specification: List[TestSpecificationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecification",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class TestSpecification(TestSpecificationType):
    """The test specification details the test specification criteria and the
    tested evaluated property(s) required for a testable object to match the
    quality or performance requirements of the business or particular
    customers.

    A test specification may contain other test specifications to form a
    hierarchy of test specifications.
    """
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class TestSpecificationInformationType:
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
    test_specification: List[TestSpecificationType] = field(
        default_factory=list,
        metadata={
            "name": "TestSpecification",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "nillable": True,
        }
    )


@dataclass
class AcknowledgeTestSpecification(AcknowledgeTestSpecificationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class AcknowledgeTestSpecificationInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["AcknowledgeTestSpecificationInformationType.DataArea"] = field(
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
        test_specification_information: List[TestSpecificationInformationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecificationInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelTestSpecification(CancelTestSpecificationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelTestSpecificationInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["CancelTestSpecificationInformationType.DataArea"] = field(
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
        test_specification_information: List[TestSpecificationInformationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecificationInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ChangeTestSpecification(ChangeTestSpecificationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangeTestSpecificationInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ChangeTestSpecificationInformationType.DataArea"] = field(
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
        test_specification_information: List[TestSpecificationInformationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecificationInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class GetTestSpecification(GetTestSpecificationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetTestSpecificationInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["GetTestSpecificationInformationType.DataArea"] = field(
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
        test_specification_information: List[TestSpecificationInformationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecificationInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessTestSpecification(ProcessTestSpecificationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessTestSpecificationInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ProcessTestSpecificationInformationType.DataArea"] = field(
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
        test_specification_information: List[TestSpecificationInformationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecificationInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class RespondTestSpecification(RespondTestSpecificationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondTestSpecificationInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["RespondTestSpecificationInformationType.DataArea"] = field(
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
        test_specification_information: List[TestSpecificationInformationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecificationInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class ShowTestSpecification(ShowTestSpecificationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowTestSpecificationInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["ShowTestSpecificationInformationType.DataArea"] = field(
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
        test_specification_information: List[TestSpecificationInformationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecificationInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class SyncTestSpecification(SyncTestSpecificationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncTestSpecificationInformationType:
    application_area: Optional[TransApplicationAreaType] = field(
        default=None,
        metadata={
            "name": "ApplicationArea",
            "type": "Element",
            "namespace": "http://www.mesa.org/xml/B2MML",
            "required": True,
        }
    )
    data_area: Optional["SyncTestSpecificationInformationType.DataArea"] = field(
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
        test_specification_information: List[TestSpecificationInformationType] = field(
            default_factory=list,
            metadata={
                "name": "TestSpecificationInformation",
                "type": "Element",
                "namespace": "http://www.mesa.org/xml/B2MML",
                "min_occurs": 1,
            }
        )


@dataclass
class TestSpecificationInformation(TestSpecificationInformationType):
    """
    Operations test information is exchanged to communicate criteria that are
    to be applied to perform tests of personnel, equipment, physical assets
    and/or materials and to communicate the results of those tests.
    """
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class AcknowledgeTestSpecificationInformation(AcknowledgeTestSpecificationInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class CancelTestSpecificationInformation(CancelTestSpecificationInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ChangeTestSpecificationInformation(ChangeTestSpecificationInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class GetTestSpecificationInformation(GetTestSpecificationInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ProcessTestSpecificationInformation(ProcessTestSpecificationInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class RespondTestSpecificationInformation(RespondTestSpecificationInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class ShowTestSpecificationInformation(ShowTestSpecificationInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"


@dataclass
class SyncTestSpecificationInformation(SyncTestSpecificationInformationType):
    class Meta:
        namespace = "http://www.mesa.org/xml/B2MML"

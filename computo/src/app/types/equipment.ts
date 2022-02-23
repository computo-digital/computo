import { HierarchyScopeType, ValueType } from '../types/common';

export interface EquipmentType {
    id: string;
    created: Date;
    modified: Date;
    description: string;
    hierarchyScope: HierarchyScopeType;
    equipmentLevel: HierarchyScopeType;
    SpatialDefinition: string;
    equipmentAssetMapping: [];
    operationalLocation: string;
    equipmentProperty: [];
    equipment: [];
    equipmentClassID: [];
    equipmentCapabilityTestSpecificationID: [];


}

export interface EquipmentPropertyType {
    id: string;
    created: Date;
    modified: Date;
    description: string;
    value: ValueType;
    equipmentProperty: [];
    evaluatedPropertyReference: [];
    testResult: [];
}

export interface OperationalLocationClassType {
    id: string;
    created: Date;
    modified: Date;
    description: string;
    hierarchyScope: object;
    operationalLocationClass: [];
    includesOperationalLocationClassID: [];
    operationalLocationID: [];
    operationalLocationClassProperty: OperationalLocationClassPropertyType[];
}

export interface OperationalLocationClassPropertyType {
    id: string;
    created: Date;
    modified: Date;
    description: string;
    value: string;
    dataType: string;
    unitOfMeasure: string;
    propertyType: [];
}
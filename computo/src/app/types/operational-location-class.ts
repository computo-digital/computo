import { HierarchyScopeType, ValueType } from '../types/common'

export interface OperationalLocationClassPropertyType {
    id: string;
    description: string;
    value: ValueType;
    propertyType: string;
}

export interface OperationalLocationClassType {
    id: string;
    description: string;
    hierarchyScope: HierarchyScopeType;
    operationalLocationClass: Array<string>;
    includesOperationalLocationClassID: Array<string>;
    operationalLocationID: Array<string>;
    operationalLocationClassProperty: Array<OperationalLocationClassPropertyType>;
}
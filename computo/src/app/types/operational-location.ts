export interface OperationalLocationType {
    id: string;
    created: Date;
    modified: Date;
    description: string;
    hierarchyScope: string;
    spatialDefinition: [];
    sperationalClassID: [];
    operationalLocation: [];
    operationalLocationProperty: OperationalLocationPropertyType[];
}

export interface OperationalLocationPropertyType {
    ID: string;
    Created: Date;
    Modified: Date;
    Description: string;
    Value: string;
    DataType: string;
    UnitOfMeasure: string;
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
}
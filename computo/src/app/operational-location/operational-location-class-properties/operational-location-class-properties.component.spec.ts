import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OperationalLocationClassPropertiesComponent } from './operational-location-class-properties.component';

describe('OperationalLocationClassPropertiesComponent', () => {
  let component: OperationalLocationClassPropertiesComponent;
  let fixture: ComponentFixture<OperationalLocationClassPropertiesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OperationalLocationClassPropertiesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OperationalLocationClassPropertiesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OperationalLocationClassFormComponent } from './operational-location-class-form.component';

describe('OperationalLocationClassFormComponent', () => {
  let component: OperationalLocationClassFormComponent;
  let fixture: ComponentFixture<OperationalLocationClassFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OperationalLocationClassFormComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OperationalLocationClassFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

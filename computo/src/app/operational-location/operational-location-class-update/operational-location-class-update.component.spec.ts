import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OperationalLocationClassUpdateComponent } from './operational-location-class-update.component';

describe('OperationalLocationClassUpdateComponent', () => {
  let component: OperationalLocationClassUpdateComponent;
  let fixture: ComponentFixture<OperationalLocationClassUpdateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OperationalLocationClassUpdateComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OperationalLocationClassUpdateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

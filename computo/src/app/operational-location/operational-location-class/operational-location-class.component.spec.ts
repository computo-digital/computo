import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OperationalLocationClassComponent } from './operational-location-class.component';

describe('OperationalLocationClassComponent', () => {
  let component: OperationalLocationClassComponent;
  let fixture: ComponentFixture<OperationalLocationClassComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OperationalLocationClassComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OperationalLocationClassComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

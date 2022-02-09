import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OperationalLocationComponent } from './operational-location.component';

describe('OperationalLocationComponent', () => {
  let component: OperationalLocationComponent;
  let fixture: ComponentFixture<OperationalLocationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OperationalLocationComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OperationalLocationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

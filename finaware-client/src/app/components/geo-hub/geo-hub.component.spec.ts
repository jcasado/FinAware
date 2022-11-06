import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GeoHubComponent } from './geo-hub.component';

describe('GeoHubComponent', () => {
  let component: GeoHubComponent;
  let fixture: ComponentFixture<GeoHubComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GeoHubComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GeoHubComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

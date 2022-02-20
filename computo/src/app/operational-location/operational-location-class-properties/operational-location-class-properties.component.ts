import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-operational-location-class-properties',
  templateUrl: './operational-location-class-properties.component.html',
  styleUrls: ['./operational-location-class-properties.component.css']
})
export class OperationalLocationClassPropertiesComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    console.log(this.route.snapshot.paramMap.get('id'));
  }

}
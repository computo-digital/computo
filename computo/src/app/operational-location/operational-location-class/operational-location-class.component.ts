import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-operational-location-class',
  templateUrl: './operational-location-class.component.html',
  styleUrls: ['./operational-location-class.component.css']
})
export class OperationalLocationClassComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    console.log('main', this.route.snapshot.paramMap.get('id'));
  }

}

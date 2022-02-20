import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-operational-location-class-update',
  templateUrl: './operational-location-class-update.component.html',
  styleUrls: ['./operational-location-class-update.component.css']
})
export class OperationalLocationClassUpdateComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    console.log(this.route.snapshot.paramMap.get('id'));
  }

}

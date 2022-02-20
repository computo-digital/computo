import { Component, OnInit } from '@angular/core';
import { AngularFirestore, AngularFirestoreDocument, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';

export interface Item { name: string; }

@Component({
  selector: 'app-operational-location-class-form',
  templateUrl: './operational-location-class-form.component.html',
  styleUrls: ['./operational-location-class-form.component.css']
})
export class OperationalLocationClassFormComponent implements OnInit {

  private itemsCollection: AngularFirestoreCollection<Item>;
  items: Observable<Item[]>;
  private itemDoc: AngularFirestoreDocument<Item>;
  private propertyDoc: AngularFirestoreDocument<Item>;
  item: Observable<Item | undefined>;
  property: Observable<Item | undefined>;
  tasks: Observable<Item[]>;

  constructor(private afs: AngularFirestore) {

    this.itemsCollection = afs.collection<Item>('OperationalLocationClass');
    this.items = this.itemsCollection.valueChanges();
    this.itemDoc = afs.doc<Item>('items/1');
    this.propertyDoc = afs.doc<Item>('items/1/tasks/OYReR2oLcQBrQ5IZ7z6G');
    this.item = this.itemDoc.valueChanges();
    this.property = this.propertyDoc.valueChanges();
    this.tasks = this.itemDoc.collection<Item>('tasks').valueChanges();
  }

  update(item: Item) {
    this.itemDoc.update(item);
  }

  ngOnInit(): void {
  }

  add(item: Item) {
    this.itemsCollection.add(item);
  }

  addItem(item: Item) {
    this.itemDoc.collection<Item>('tasks').add(item);
  }

}

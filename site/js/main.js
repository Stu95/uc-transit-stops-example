import stops from '../data/stops.js';
import { initializeStopMap, showStopsOnMap } from './stops-map.js';

let stopMap = initializeStopMap();
showStopsOnMap(stops, stopMap);

let routeCheckboxes = document.querySelectorAll('.route-checkbox');

for (const cb of routeCheckboxes) {
  cb.addEventListener('change', (evt) => {
    console.log('you clicked on a checkbox');
    console.log(evt.target);
  });
}

window.stops = stops;
window.routeCheckboxes = routeCheckboxes;

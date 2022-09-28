import stops from '../data/stops.js';
import { initializeStopMap, showStopsOnMap } from './stops-map.js';

let stopMap = initializeStopMap();
showStopsOnMap(stops, stopMap);

let routeCheckboxes = document.querySelectorAll('.route-checkbox');
let stopNameInput = document.querySelector('#stop-name-input');

for (const cb of routeCheckboxes) {
  cb.addEventListener('change', (evt) => {
    console.log('you clicked on a checkbox');
    console.log(evt.target);
  });
}

stopNameInput.addEventListener('input', () => {
  const text = stopNameInput.value;
  const filteredStops = stops.filter(function (stop) {
    const name = stop['stop_name'].toLowerCase();
    const hasText = name.includes(text);
    return hasText;
  });
  showStopsOnMap(filteredStops, stopMap);
});

window.stops = stops;
window.stopMap = stopMap;
window.routeCheckboxes = routeCheckboxes;

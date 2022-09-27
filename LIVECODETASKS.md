- [X] Create an _index.html_ with a basic HTML page structure
- [X] Create an empty CSS file for the project
- [X] Create an empty JavaScript file for the project
- [X] Link to the empty CSS file from the bottom of the `head` of your HTML file
- [X] Link to the empty JavaScript file from the bottom of the `body` of your HTML file
- [X] Add a level-1 heading (`h1`) to the body with the app title, just so there's something to see on the page

Check the app in the browser.

- [X] Add a Leaflet map for displaying the list of stops to the page
- [X] Import the data from _site/data/stops.js_ into your JavaScript file.
- [X] Import the data from _site/data/universitycity.js_ into your JavaScript file.
- [X] Add the University City shape to the map. Style it so that it has some pop.

- [X] Create a function called `makeStopFeature` to transform one of the stop elements into a GeoJSON-like feature.
- [X] Use the function to display all the `stops` data on the map.
- [X] Create a function to show an array of stops on the map. Call the function `showStopsOnMap`

- [ ] Create a list element (unordered -- `ul`) in the HTML give it an id of `stop-list`
- [ ] Write a function that fills in the list with list item (`li`) elements for each stop in an array
- [ ] Add a checkbox for each route in University City.
- [ ] Add a text box to filter stops whose name contains a given string. The text box should have an id of `stop-name-filter`.
- [ ] Write a predicate function called `shouldShowStop` that will return `true` if a given stop should be shown according to the currently selected filters, and will return `false` if a given stop should not be shown. For now, ignore the filters and always return `true`.

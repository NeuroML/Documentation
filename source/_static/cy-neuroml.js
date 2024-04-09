Promise.all([
    fetch('cy-style.json')
      .then(function(res) {
        return res.json();
      }),
    fetch('neuroml.json')
      .then(function(res) {
        return res.json();
      })
  ])
  .then(function(dataArray) {
    const style = dataArray[0];
    const elements = dataArray[1];
    console.log(elements);
    cy = window.cy = cytoscape({
        container: document.getElementById('cy'),
        elements: elements,
        layout: { name: 'random' },
        style: style
    });
    //cy.on("select", "*", highlightElement);
    //cy.on("unselect", "*", unhighlightNode);
    // cy.on("dragfree", "*", function(event) {
    //     cy_layout.stop();
    //     event.target.lock();
    //     cy_layout.run();
    //     event.target.unlock();
    // });
    cy_layout = cy.layout({
        name: "concentric",
        avoidOverlap: true,
        centerGraph: true,
        fit: true,
    });
    cy_layout.run();
    }
  );

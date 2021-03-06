class Treemap {

  constructor() {

    this.svg = d3.select("svg");
    this.width = +this.svg.attr("width");
    this.height = +this.svg.attr("height");

    this.fader = function(color) { return d3.interpolateRgb(color, "#fff")(0.2); };
    //this.color = d3.scaleOrdinal(d3.schemeCategory20.map(this.fader));

    this.color = {
      'PT': '#99060c',
      'PSDB': '#0a5b9d',
      'PV': '#006600',
      'NOVO': '#f7833b',
      'PSOL': '#fedf0a',
      'DEM': '#91e9f5',
      'PP': '#005ea4',
      'PTB': '#232323',
      'PRB': '#0089ad',
      'PMDB': '#49ae34',
      'PR': '#dc352f',
      'PSB': '#f12e3c',
      'PSD': '#80c342',
      'PPS': '#ff3124',
      'PSC': '#00923e',
      'PROS': '#faa13b',
      'PHS': '#8a191e',
      'PTN': '#00d663'
    }
    this.format = d3.format(",d");

    this.data = null;
    this.root = null;

    this.treemap = d3.treemap()
      .tile(d3.treemapResquarify)
      .size([this.width, this.height])
      .round(true)
      .paddingInner(1);

    d3.select("#atualizar")
      .on("click", d => {
        let svg = document.getElementById("svg");
        svg.innerHTML = "";
        this.buildChart(d3.select("#order").node().value);

      });

  }

  loadDataAndCreateChart() {
    d3.json("/vereadores/treemap.json", (error, data) => {
      if (error) throw error;

      this.data = data;

      this.buildChart(1);

    });
  }

  buildChart(view) {

    let f = this.sumByDonations;
    if (view == 1) {
      f = this.sumBySize;
    } else if (view == 2) {
      f = this.sumByDonations;
    } else if (view == 3) {
      f = this.sumByAssets;
    } else if (view == 4) {
      f = this.sumByElectionExpense;
    } else {
      f = this.sumByExpenses;
    }

    this.root = d3.stratify()
      .id(function(d) { return d.name; })
      .parentId(d => {
        if (view == 1) {
          return d.party;
        } else {
          return d.parent;
        }
      })
      (this.data)
      .eachBefore(
        function(d) { d.data.id = (d.parent ? d.parent.data.id + "." : "") + d.data.name; }
      )
      .sum(f)
      .sort(function(a, b) { return b.height - a.height || b.value - a.value; });

    this.treemap(this.root);

    this.cell = this.svg.selectAll("g")
      .data(this.root.leaves())
      .enter().append("g")
        .attr("transform", function(d) { return "translate(" + d.x0 + "," + d.y0 + ")"; });

    this.cell.append("rect")
      .attr("id", function(d) { return d.data.id; })
      .attr("width", function(d) { return d.x1 - d.x0; })
      .attr("height", function(d) { return d.y1 - d.y0; })
      .attr("fill", d => this.color[d.data.party] )
      .attr("style", "cursor: pointer")
      .on("click", function(d) { window.location = "/vereadores/" + d.data.slug });

    this.cell.append("clipPath")
      .attr("id", function(d) { return "clip-" + d.data.id; })
      .append("use")
      .attr("xlink:href", function(d) { return "#" + d.data.id; });

    this.cell.append("text")
      .attr("clip-path", function(d) { return "url(#clip-" + d.data.id + ")"; })
      .attr("class", function(d) { return d.data.party })
      .selectAll("tspan")
      .data(function(d) { return d.data.name.split(/(?=[A-Z][^A-Z])/g); })
        .enter().append("tspan")
          .attr("x", 4)
          .attr("style", "cursor: pointer; margin-bottom: 12px")
          .attr("y", function(d, i) { return i * 10 + 15; })
          .text(function(d) { return d; })
          .on("click", function(d) { window.location = "/vereadores/" + d.data.slug });

    this.cell.append("title")
      .text(function(d) { return d.data.party; });
  }

  sumBySize(d) {
    return d.size;
  }

  sumByDonations(d) {
    return d.donations;
  }

  sumByAssets(d) {
    return d.assets;
  }

  sumByElectionExpense(d) {
    return d.election_expenses;
  }

  sumByExpenses(d) {
    return d.expenses;
  }

}

- dashboard: campaign_performance_portfolio
  title: "Paid Media Performance & Acquisition — Synthetic Data"
  layout: newspaper
  preferred_viewer: dashboards-next
  elements:
  - name: primary_view
    title: "Paid Media Performance & Acquisition"
    model: marketing
    explore: campaign_performance
    type: looker_column
    fields: [campaign_performance.channel, campaign_performance.cac]
    row: 0
    col: 0
    width: 24
    height: 10

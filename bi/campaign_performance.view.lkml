view: campaign_performance {
  sql_table_name: analytics.campaign_daily ;;
  dimension: channel { type: string sql: ${TABLE}.channel ;; }
  dimension: platform { type: string sql: ${TABLE}.platform ;; }
  dimension: geography { type: string sql: ${TABLE}.geography ;; }
  dimension: audience { type: string sql: ${TABLE}.audience ;; }
  dimension: campaign_id { type: string sql: ${TABLE}.campaign_id ;; }
  dimension_group: activity { type: time timeframes: [date, week, month] sql: ${TABLE}.date ;; }
  measure: spend { type: sum sql: ${TABLE}.spend_usd ;; value_format_name: usd }
  measure: impressions { type: sum sql: ${TABLE}.impressions ;; }
  measure: clicks { type: sum sql: ${TABLE}.clicks ;; }
  measure: members { type: sum sql: ${TABLE}.new_members ;; }
  measure: net_revenue { type: sum sql: ${TABLE}.net_revenue_usd ;; value_format_name: usd }
  measure: cac { type: number sql: 1.0 * ${spend} / NULLIF(${members},0) ;; value_format_name: usd }
  measure: ctr { type: number sql: 1.0 * ${clicks} / NULLIF(${impressions},0) ;; value_format_name: percent_2 }
  measure: roas { type: number sql: 1.0 * ${net_revenue} / NULLIF(${spend},0) ;; value_format_name: decimal_2 }
}

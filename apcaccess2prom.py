#!/usr/bin/env python3

import fileinput

metric_prefix="apcupsd"

labels = [
  { "name" : "upsname", "value" : "main"},
  { "name" : "upstype", "value" : "standalone"}
  ]

series = {
  "LINEV"     : "line_volts",
  "LOADPCT"   : "output_load_percent",
  "BCHARGE"   : "battery_charge_current_percent",
  "TIMELEFT"  : "baterry_time_left_seconds",
  "MBATTCHG"  : "battery_charge_minimal_percent",
  "MINTIMEL"  : "battery_min_runtime_to_shutdown_seconds",
  "MAXTIME"   : "battery_max_runtime_to_shutdown_seconds",
  "OUTPUTV"   : "output_volts",
  "DWAKE"     : "ups_wakeup_delay_seconds",
  "DSHUTD"    : "ups_shutdown_delay_seconds",
  "LOTRANS"   : "input_low_threshold_volts",
  "HITRANS"   : "input_high_threshold_volts",
  "RETPCT"    : "battery_minimal_wakeup_level_percent",
  "ITEMP"     : "ups_internal_temperature_celsius",
  "BATTV"     : "battery_volts",
  "LINEFREQ"  : "line_frequency_hertz",
  "NUMXFERS"  : "ups_transfers_total",
  "TONBATT"   : "ups_onbatt_seconds",
  "CUMONBATT" : "ups_onbatt_seconds_sum",
  "NOMOUTV"   : "optput_nominal_volts",
  "NOMINV"    : "input_nominal_volts",
  "NOMBATTV"  : "battery_nominal_volts",
  "NOMPOWER"  : "output_nominal_watts"
}

out = {}

for line in fileinput.input():
  l = line.strip().split(':')
  key = l[0].strip()
  if key in series.keys():
    value = float(l[1].strip().split(' ')[0])
    out["%s_%s" % (metric_prefix, series[key])] = value

labelss = ', '.join(["%s=\"%s\"" % (l['name'], l['value']) for l in labels ])
  
for metric, value in out.items():
  print("%s{%s} %.2f" % (metric, labelss, value))


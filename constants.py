url = 'https://renesas.evmlabs.com/user/form60dc441fc555b005b68d0e9f?APP=5f12f3d2c555b026c55ae500'
Connect_Button = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form/label/span'
Live_Button = '//*[@id="render-main"]/div[1]/div[1]/div/ul/li[2]'
Three_Watt_Button = '//*[@id="stepformcontainer"]/tx-elements[1]/div[2]/div/div/div/span[1]'
Eight_Watt_Button = '//*[@id="stepformcontainer"]/tx-elements[1]/div[2]/div/div/div/span[2]'
Eleven_Watt_Button = '//*[@id="stepformcontainer"]/tx-elements[1]/div[2]/div/div/div/span[3]'
Next_Button = '//*[@id="stepformcontainer"]/tx-elements[4]/div[2]/div/div/div/button'
Previous_Button = '//*[@id="stepformcontainer"]/tx-elements[3]/div[2]/div/div/div/button'
Led_Button = '//*[@id="stepformcontainer"]/tx-elements[6]/div[2]/div/div/div/button'
Temp_Button = '//*[@id="stepformcontainer"]/tx-elements[7]/div[2]/div/div/div/button'
Humidity_Button = '//*[@id="stepformcontainer"]/tx-elements[8]/div[2]/div/div/div/button'
Graph_Open_Button = '//*[@id="c64edc5c-b53d-fe87-2bbc-d2b18f64e023"]/div/tx-elements/div[2]/div/div[1]/div[2]/em'
Graph_Close_Button = '//*[@id="c64edc5c-b53d-fe87-2bbc-d2b18f64e023"]/div/tx-elements/div[2]/div/div[1]/div[2]/em'
Video_Open_button = '//*[@id="e00b90ab-27bb-53fa-7437-7f676d99107c"]/div/tx-elements/div[2]/div/div/div[1]/div/div[1]'
Graph_Image = '//*[@id="c64edc5c-b53d-fe87-2bbc-d2b18f64e023"]/div/tx-elements/div[2]/div'
Video_Image = '//*[@id="e00b90ab-27bb-53fa-7437-7f676d99107c"]/div/tx-elements/div[2]/div/div'
Video_Close_Button = '//*[@id="e00b90ab-27bb-53fa-7437-7f676d99107c"]/div/tx-elements/div[2]/div/div/div[1]/div/div[1]'
Disconnect_Button = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form/label/span'
Three_watt_Battery = '//*[@id="eae56553-5125-2748-f500-429dc77de6c6"]'
Full_screen = 'https://renesas.evmlabs.com/user/form60dc441fc555b005b68d0e9f?APP=5f12f3d2c555b026c55ae500'
progress_log = '//*[@id="console_status"]/div/tx-elements/div[2]/div/ul'

# ---------------------------------------------------JP128-------------------------------------------------------------




# -------------------------------------------- US-069 START---------------------------------------------------------

On_US069 = '//*[@id="stepformcontainer"]/tx-elements[1]/div[2]/div/div/div/span[1]/label'

Slider_move_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[' \
                    '5]/div/div/tx-elements/div[2]/div[1]/div[2]/ng-content[1]/ng-content/tx-elements/div[' \
                    '2]/div/div/form/tx-elements[3]/div[2]/div/div/div[2]/span[9] '

US069_url = 'https://renesas.evmlabs.com/user/form612ccda5c555b07e335ad926?APP=5f12f3d2c555b026c55ae500'

Rpm_graph_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[' \
                  '2]/div/div/tx-elements/div[2]/div[1]/div[1]/ul/li[2]/a '

Motor_graph_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[' \
                    '2]/div/div/tx-elements/div[2]/div[1]/div[1]/ul/li[3]/a '

Video_refresh_US069 = '/html/body/div[2]/div[2]/div/button'

Maximize_live_video_US069 = '//*[@id="bb75c1eb-1f0b-9c64-685f-3b983adfc69b"]/div/tx-elements/div[2]/div/div/div[' \
                            '1]/div/div[1] '

Live_video_path_US069 = '//*[@id="bb75c1eb-1f0b-9c64-685f-3b983adfc69b"]/div/tx-elements/div[2]/div/div'

Switch_charging_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[' \
                        '2]/div/div/div/div/ul/li[5]/div/div/tx-elements/div[2]/div[1]/div[1]/ul/li[2]/a '

Charging_voltage_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[' \
                         '2]/div/div/div/div/ul/li[5]/div/div/tx-elements/div[2]/div[1]/div[2]/ng-content[' \
                         '2]/ng-content/tx-elements/div[2]/div/div/form/tx-elements[2]/div[2]/div/div/select '

Set_60V_Us069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[' \
                '5]/div/div/tx-elements/div[2]/div[1]/div[2]/ng-content[2]/ng-content/tx-elements/div[' \
                '2]/div/div/form/tx-elements[2]/div[2]/div/div/select/option[5] '

Start_charging_US069 = '//*[@id="stepformcontainer"]/tx-elements[6]/div[2]/div/div/div/button'

Battery_voltage_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[' \
                        '2]/div/div/div/div/ul/li[5]/div/div/tx-elements/div[2]/div[1]/div[2]/ng-content[' \
                        '2]/ng-content/tx-elements/div[2]/div/div/form/tx-elements[3]/div[2]/div/div/select '

Set_54V_Us069 = '//*[@id="select_id83578c3d-d311-7eac-e26a-5764b5d27909"]/option[5]'

Battery_current_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[' \
                        '2]/div/div/div/div/ul/li[5]/div/div/tx-elements/div[2]/div[1]/div[2]/ng-content[' \
                        '2]/ng-content/tx-elements/div[2]/div/div/form/tx-elements[4]/div[2]/div/div/select '

Set_4A_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[' \
               '5]/div/div/tx-elements/div[2]/div[1]/div[2]/ng-content[2]/ng-content/tx-elements/div[' \
               '2]/div/div/form/tx-elements[4]/div[2]/div/div/select/option[4] '

Maximize_graph_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[' \
                       '2]/div/div/div/div/ul/li[2]/div/div/tx-elements/div[2]/div[1]/div[2]/ng-content[' \
                       '1]/ng-content/tx-elements/div[2]/div/div[1]/div[2] '

Time_graph_US069 = '//*[@id="833413ae-1d11-a2eb-fbb0-9acb82e244c8"]/ng-content/tx-elements/div[2]/div/div[1]/div[2]'

Time_graph_path = '//*[@id="833413ae-1d11-a2eb-fbb0-9acb82e244c8"]/ng-content/tx-elements/div[2]/div'

Maximize_ram_US069 = '//*[@id="7f4f430a-35dd-581a-1b37-42a3561562f1"]/ng-content/tx-elements/div[2]/div/div[1]/div[2]'

Graph_path_US069 = '//*[@id="833413ae-1d11-a2eb-fbb0-9acb82e244c8"]/ng-content/tx-elements/div[2]/div'

Live_parameters_US069 = '//*[@id="c5712e9e-0ac9-fb69-dda4-f424b7298cc0"]'

Stop_charging_US069 = '//*[@id="stepformcontainer"]/tx-elements[7]/div[2]/div/div/div/button'

Rpm_graph_path = '//*[@id="7f4f430a-35dd-581a-1b37-42a3561562f1"]/ng-content/tx-elements/div[2]/div'

Maximize_motor_US069 = '//*[@id="7ce00a36-3803-6c25-de6f-e85bd3711d97"]/ng-content/tx-elements/div[2]/div/div[1]/div[2]'

Motor_graph_path = '//*[@id="7ce00a36-3803-6c25-de6f-e85bd3711d97"]/ng-content/tx-elements/div[2]/div'

Time_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[' \
             '2]/div/div/tx-elements/div[2]/div[1]/div[1]/ul/li[1]/a '

Click_off_US069 = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[' \
                  '5]/div/div/tx-elements/div[2]/div[1]/div[2]/ng-content[1]/ng-content/tx-elements/div[' \
                  '2]/div/div/form/tx-elements[1]/div[2]/div/div/div/span[2]/label '

Maximize_Live_video_one = '//*[@id="bb75c1eb-1f0b-9c64-685f-3b983adfc69b"]/div/tx-elements/div[2]/div/div/div[' \
                          '1]/div/div[1] '

Live_video_path_one = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div[' \
                      '2]/div/div/div/div/ul/li[1]/div/div/tx-elements/div[2]/div/div'

# -------------------------------------------- EU-036 START---------------------------------------------------------

EU036_url = 'https://renesas.evmlabs.com/user/form61239510c555b04ec32b5827?APP=5f12f3d2c555b026c55ae500'

Live_video_path_EU036 = '//*[@id="785b567d-5414-edfb-01da-d05b1ae2d49e"]/div/tx-elements/div[2]/div/div'

Maximize_live_EU036 = '//*[@id="785b567d-5414-edfb-01da-d05b1ae2d49e"]/div/tx-elements/div[2]/div/div/div[1]/div/div[1]'

Temp_Button_EU036 = '//*[@id="stepformcontainer"]/tx-elements[1]/div[2]/div/div/div/div/label/span'

Live_video_display_EU036 = '//*[@id="d61bd242-7f84-d9fe-0109-47516b2f962b"]/div/tx-elements/div[2]/div/div/div[' \
                           '1]/div/div[1] '

Display_live_video_path = '/html/body/div[2]'

# -------------------------------------------- RZ_A2M START---------------------------------------------------------

RZ_url = 'https://renesas.evmlabs.com/user/form6156cdf2c555b031526608e1?APP=5f12f3d2c555b026c55ae500'

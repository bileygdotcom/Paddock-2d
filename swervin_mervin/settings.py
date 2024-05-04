from pygame import Color
import math, os

FPS                   = 60
TITLE_FPS             = 20
COUNTDOWN_FPS         = 1
PLAYER_SELECT_FPS     = 10
CREDITS_FPS           = 10
LEVEL_OVER_LAG        = 4 * FPS
TITLE_SCREEN          = True
COUNTDOWN             = True
PLAYER_SELECT         = True
FULLSCREEN            = True
FRAME_RATE            = (1.0 / FPS)
DIMENSIONS            = (1366,768)
#DIMENSIONS            = (800, 600)
#DIMENSIONS            = (1024, 768)
#DIMENSIONS            = (640, 480)
MUSIC_VOLUME          = 0.7
SEGMENT_HEIGHT        = 260
RUMBLE_LENGTH         = 3
DRAW_DISTANCE         = 125
ROAD_WIDTH            = 3000
LANES                 = 4
BOUNDS                = 1.5
TUNNEL_BOUNDS         = 0.85
TUNNEL_HEIGHT         = 150
TUNNEL_LIGHT_FREQ     = 15
AUTO_DRIVE            = False
PLAYER_ANIM_HOLD      = 8
CHECKPOINT            = 81
LAP_DIFFICULTY_FACTOR = 2
LAPS_PER_LEVEL        = 3
MINIMUM_DIFFICULTY    = 3
MINIMUM_ENGINE_DIST   = 4000
#CRASH_DIVISOR         = 1
POINTS                = 15
CHANCE_OF_BONUSES     = 10
BONUS_AMOUNT          = 20
POINT_GAIN_PROSTITUTE = 500
POINT_LOSS_SPRITE     = 0.5
POINT_LOSS_COMP       = 0.5
POINT_MILESTONE       = 20000
MINIMUM_CORNER_SMOKE  = 3
FIELD_OF_VIEW         = 120 # Degrees
CAMERA_HEIGHT         = 1200
CAMERA_DEPTH          = 1 / math.tan((FIELD_OF_VIEW / 2) * math.pi / 180)
BOTTOM_OFFSET         = 100
SPEED_BOOST_DECREASE  = 0.04
SPEED_BOOST_LENGTH    = 50
HARD_TOP_SPEED        = [(SEGMENT_HEIGHT / (1.0/FPS)) * 1.5, (SEGMENT_HEIGHT / (1.0/FPS)) * 2.4]
HARD_HANDLING         = [0.1, 0.45]
HARD_ACCELERATION     = [1.0, 60.0]
PLAYER_Z              = (CAMERA_HEIGHT * CAMERA_DEPTH)
FONTS                 = {"retro_computer": os.path.join("lib","fonts","IndieFlower-Regular.ttf"),
                         "fipps": os.path.join("lib", "fonts", "Fipps-Regular.otf")}
COLOURS               = {"white": Color(255, 255, 255),
                         "opaque_white": Color(155, 155, 155, 80),
                         "text": Color(172, 199, 252),
                         "dark_text": Color(57, 84, 137),
                         "selection": [Color(172, 199, 252),Color(100, 149, 252)],
                         "sky": Color(10, 10, 10),
                         "gutter": Color(100, 100, 100),
                         "red": Color(204, 0, 0),
                         "bonus_a": Color(255, 78, 0),
                         "bonus_b": Color(255, 178, 0),
                         "green": Color(0, 204, 0),
                         "black": Color(0, 0, 0),
                         "tunnel": Color(38, 15, 8)}
LEVELS             = [{"id": "01-01",
                       "name": "Cherepovets #1. From Vologda.",
                       "song": "lazerhawk-overdrive.ogg",
                       "laps": 1,
                       "colours": {
                         "wall":  Color(32, 32, 32),
                         "light": {"road":     Color(34, 54, 56),
                                   "grass":    Color(0, 50, 30),
                                   "footpath": Color(53, 50, 30),
                                   "line":     Color(185, 185, 185)},
                         "dark":  {"road":     Color(48, 64, 81),
                                   "grass":    Color(0, 36, 16),
                                   "footpath": Color(34, 36, 16),
                                   "line":     Color(185, 185, 185)}},
                       "backgrounds": [
                         {"id": "far_cherepovets_bac",
                          "speed": 2,
                          "convert": True,
                          "scale": False},
                         {"id": "far_cherepovets",
                          "speed": 1,
                          "convert": False,
                          "scale": True}
                       ]},
                      {"id": "01-02",
                       "name": "Cherepovets #2. A114.",
                       "song": "lazerhawk-overdrive.ogg",
                       "laps": 1,
                       "colours": {
                         "wall":  Color(32, 32, 32),
                         "light": {"road":     Color(34, 54, 56),
                                   "grass":    Color(0, 50, 30),
                                   "footpath": Color(53, 50, 30),
                                   "line":     Color(185, 185, 185)},
                         "dark":  {"road":     Color(48, 64, 81),
                                   "grass":    Color(0, 36, 16),
                                   "footpath": Color(34, 36, 16),
                                   "line":     Color(185, 185, 185)}},
                       "backgrounds": [
                         {"id": "far_cherepovets_bac",
                          "speed": 2,
                          "convert": True,
                          "scale": False},
                         {"id": "far_cherepovets",
                          "speed": 1,
                          "convert": False,
                          "scale": True}
                       ]},
                      {"id": "01-03",
                       "name": "Cherepovets #3. Suburbs.",
                       "song": "lazerhawk-overdrive.ogg",
                       "laps": 1,
                       "colours": {
                         "wall":  Color(32, 32, 32),
                         "light": {"road":     Color(34, 54, 56),
                                   "grass":    Color(0, 50, 30),
                                   "footpath": Color(53, 50, 30),
                                   "line":     Color(185, 185, 185)},
                         "dark":  {"road":     Color(48, 64, 81),
                                   "grass":    Color(0, 36, 16),
                                   "footpath": Color(34, 36, 16),
                                   "line":     Color(185, 185, 185)}},
                       "backgrounds": [
                         {"id": "far_cherepovets_bac",
                          "speed": 2,
                          "convert": True,
                          "scale": False},
                         {"id": "far_cherepovets",
                          "speed": 1,
                          "convert": False,
                          "scale": True}
                       ]},
                      {"id": "02-01",
                       "name": "Saint Petersburg #1: ZSD over Gulf",
                       "song": "timecop1983-summerheat.ogg",
                       "laps": 1,
                       "colours": {
                         "wall":  Color(32, 32, 32),
                         "light": {"road":     Color(34, 54, 56),
                                   "grass":    Color(0, 30, 70),
                                   "footpath": Color(82, 96, 115),
                                   "line":     Color(185, 185, 185)},
                         "dark":  {"road":     Color(48, 64, 81),
                                   "grass":    Color(0, 16, 56),
                                   "footpath": Color(68, 84, 101),
                                   "line":     Color(185, 185, 185)}},
                       "backgrounds": [
                         {"id": "far_saint-p_bac",
                          "speed": 2,
                          "convert": True,
                          "scale": False},
                         {"id": "far_saint-p",
                          "speed": 1,
                          "convert": False,
                          "scale": True},
                       ]},
                      {"id": "02-02",
                       "name": "Saint Petersburg #2: Kupchino",
                       "song": "timecop1983-summerheat.ogg",
                       "laps": 1,
                       "colours": {
                         "wall":  Color(32, 32, 32),
                         "light": {"road":     Color(34, 54, 56),
                                   "grass":    Color(32, 32, 32),
                                   "footpath": Color(82, 96, 115),
                                   "line":     Color(185, 185, 185)},
                         "dark":  {"road":     Color(48, 64, 81),
                                   "grass":    Color(16, 16, 16),
                                   "footpath": Color(68, 84, 101),
                                   "line":     Color(185, 185, 185)}},
                       "backgrounds": [
                         {"id": "far_saint-p_bac",
                          "speed": 2,
                          "convert": True,
                          "scale": False},
                         {"id": "far_saint-p",
                          "speed": 1,
                          "convert": False,
                          "scale": True},
                       ]},
                      {"id": "02-03",
                       "name": "Saint Petersburg #2: E-95",
                       "song": "lazerhawk-overdrive.ogg",
                       "laps": 1,
                       "colours": {
                         "wall":  Color(32, 32, 32),
                         "light": {"road":     Color(34, 54, 56),
                                   "grass":    Color(0, 50, 30),
                                   "footpath": Color(53, 50, 30),
                                   "line":     Color(185, 185, 185)},
                         "dark":  {"road":     Color(48, 64, 81),
                                   "grass":    Color(0, 36, 16),
                                   "footpath": Color(34, 36, 16),
                                   "line":     Color(185, 185, 185)}},
                       "backgrounds": [
                         {"id": "far_saint-p_bac",
                          "speed": 2,
                          "convert": True,
                          "scale": False},
                         {"id": "far_saint-p",
                          "speed": 1,
                          "convert": False,
                          "scale": True}
                       ]},
                      {"id": "nullarbor",
                       "name": "Sochi",
                       "song": "alvernagunn-maddog.ogg",
                       "laps": 1,
                       "colours": {
                         "wall":  Color(92, 92, 92),
                         "light": {"road":     Color(64, 84, 86),
                                   "grass":    Color(135, 198, 86),
                                   "footpath": Color(112, 126, 145),
                                   "line":     Color(185, 185, 185)},
                         "dark":  {"road":     Color(78, 94, 111),
                                   "grass":    Color(96, 187, 74),
                                   "footpath": Color(98, 114, 131),
                                   "line":     Color(185, 185, 185)}},
                       "backgrounds": [
                         {"id": "far_sochi_bac",
                          "speed": 2,
                          "convert": True,
                          "scale": False},
                         {"id": "far_sochi",
                          "speed": 1,
                          "convert": False,
                          "scale": True},
                       ]}
                     ]
PLAYERS            = [{"name": "#77 Porsche 959",
                       "age": 48,
                       "top_speed": (SEGMENT_HEIGHT / (1.0/FPS)) * 3.5 * 1.0,
                       "offroad_top_speed_factor": 7.0,
                       "acceleration_factor": 2.2,
                       "deceleration": 3.0,
                       "centrifugal_force": 0.26,
                       "city": "blow head speed",
                       "select_sfx": "swervin_mervin_select.ogg",
                       "sprites":
                         {"mugshot_small": {
                           "path": "77_sm.png",
                           "width": 50,
                           "height": 30},
                          "mugshot_large": {
                           "path": "77_w.png",
                           "width": 500,
                           "height": 300},
                          "straight1": {
                           "path": "S_P_C_1.png",
                           "width": 100,
                           "height": 84},
                          "straight2": {
                           "path": "S_P_C_2.png",
                           "width": 100,
                           "height": 84},
                          "left1": {
                           "path": "L_P_C_1.png",
                           "width": 118,
                           "height": 84},
                          "left2": {
                           "path": "L_P_C_2.png",
                           "width": 118,
                           "height": 84},
                          "right1": {
                           "path": "R_P_C_1.png",
                           "width": 118,
                           "height": 84},
                          "right2": {
                           "path": "R_P_C_2.png",
                           "width": 118,
                           "height": 84},
                          "left_smoke1": {
                           "path": "L_P_S_1.png",
                           "width": 118,
                           "height": 84},
                          "left_smoke2": {
                           "path": "L_P_S_2.png",
                           "width": 118,
                           "height": 84},
                          "right_smoke1": {
                           "path": "R_P_S_1.png",
                           "width": 118,
                           "height": 84},
                          "right_smoke2": {
                           "path": "R_P_S_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_straight1": {
                           "path": "S_U_C_1.png",
                           "width": 100,
                           "height": 84},
                          "uphill_straight2": {
                           "path": "S_U_C_2.png",
                           "width": 100,
                           "height": 84},
                          "uphill_left1": {
                           "path": "L_U_C_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_left2": {
                           "path": "L_U_C_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right1": {
                           "path": "R_U_C_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right2": {
                           "path": "R_U_C_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_left_smoke1": {
                           "path": "L_U_S_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_left_smoke2": {
                           "path": "L_U_S_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right_smoke1": {
                           "path": "R_U_S_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right_smoke2": {
                           "path": "R_U_S_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_straight1": {
                           "path": "S_D_C_1.png",
                           "width": 100,
                           "height": 84},
                          "downhill_straight2": {
                           "path": "S_D_C_2.png",
                           "width": 100,
                           "height": 84},
                          "downhill_left1": {
                           "path": "L_D_C_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_left2": {
                           "path": "L_D_C_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right1": {
                           "path": "R_D_C_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right2": {
                           "path": "R_D_C_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_left_smoke1": {
                           "path": "L_D_S_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_left_smoke2": {
                           "path": "L_D_S_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right_smoke1": {
                           "path": "R_D_S_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right_smoke2": {
                           "path": "R_D_S_2.png",
                           "width": 118,
                           "height": 84}}},
                       {"name": "#94 Dodge Shelby Daytona",
                        "age": 21,
                        "top_speed": (SEGMENT_HEIGHT / (1.0/FPS)) * 2.0 *2.0,
                        "offroad_top_speed_factor": 3.0,
                        "acceleration_factor": 7.0,
                        "deceleration": 3.0,
                        "centrifugal_force": 0.16,
                        "city": "Fastest of all US over",
                        "select_sfx": "candy_select.ogg",
                        "sprites":
                         {"mugshot_small": {
                           "path": "94_sm.png",
                           "width": 50,
                           "height": 30},
                          "mugshot_large": {
                           "path": "94_w.png",
                           "width": 500,
                           "height": 300},
                          "straight1": {
                           "path": "94_S_P_C_1.png",
                           "width": 100,
                           "height": 84},
                          "straight2": {
                           "path": "94_S_P_C_2.png",
                           "width": 100,
                           "height": 84},
                          "left1": {
                           "path": "94_L_P_C_1.png",
                           "width": 118,
                           "height": 84},
                          "left2": {
                           "path": "94_L_P_C_2.png",
                           "width": 118,
                           "height": 84},
                          "right1": {
                           "path": "94_R_P_C_1.png",
                           "width": 118,
                           "height": 84},
                          "right2": {
                           "path": "94_R_P_C_2.png",
                           "width": 118,
                           "height": 84},
                          "left_smoke1": {
                           "path": "94_L_P_S_1.png",
                           "width": 118,
                           "height": 84},
                          "left_smoke2": {
                           "path": "94_L_P_S_2.png",
                           "width": 118,
                           "height": 84},
                          "right_smoke1": {
                           "path": "94_R_P_S_1.png",
                           "width": 118,
                           "height": 84},
                          "right_smoke2": {
                           "path": "94_R_P_S_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_straight1": {
                           "path": "94_S_U_C_1.png",
                           "width": 100,
                           "height": 84},
                          "uphill_straight2": {
                           "path": "94_S_U_C_2.png",
                           "width": 100,
                           "height": 84},
                          "uphill_left1": {
                           "path": "94_L_U_C_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_left2": {
                           "path": "94_L_U_C_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right1": {
                           "path": "94_R_U_C_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right2": {
                           "path": "94_R_U_C_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_left_smoke1": {
                           "path": "94_L_U_S_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_left_smoke2": {
                           "path": "94_L_U_S_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right_smoke1": {
                           "path": "94_R_U_S_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right_smoke2": {
                           "path": "94_R_U_S_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_straight1": {
                           "path": "94_S_D_C_1.png",
                           "width": 100,
                           "height": 84},
                          "downhill_straight2": {
                           "path": "94_S_D_C_2.png",
                           "width": 100,
                           "height": 84},
                          "downhill_left1": {
                           "path": "94_L_D_C_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_left2": {
                           "path": "94_L_D_C_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right1": {
                           "path": "94_R_D_C_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right2": {
                           "path": "94_R_D_C_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_left_smoke1": {
                           "path": "94_L_D_S_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_left_smoke2": {
                           "path": "94_L_D_S_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right_smoke1": {
                           "path": "94_R_D_S_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right_smoke2": {
                           "path": "94_R_D_S_2.png",
                           "width": 118,
                           "height": 84}}},
                       {"name": "#73 Mitsubishi Starion",
                        "age": 37,
                        "top_speed": (SEGMENT_HEIGHT / (1.0/FPS)) * 2.556 * 2.0,
                        "offroad_top_speed_factor": 4.0,
                        "acceleration_factor": 6.0,
                        "deceleration": 2.5,
                        "centrifugal_force": 0.22,
                        "city": "Japaneese star wars lion",
                        "select_sfx": "burl_select.ogg",
                        "sprites":
                         {"mugshot_small": {
                           "path": "73_sm.png",
                           "width": 50,
                           "height": 30},
                          "mugshot_large": {
                           "path": "73_w.png",
                           "width": 840,
                           "height": 450},
                          "straight1": {
                           "path": "73_S_P_C_1.png",
                           "width": 100,
                           "height": 84},
                          "straight2": {
                           "path": "73_S_P_C_2.png",
                           "width": 100,
                           "height": 84},
                          "left1": {
                           "path": "73_L_P_C_1.png",
                           "width": 118,
                           "height": 84},
                          "left2": {
                           "path": "73_L_P_C_2.png",
                           "width": 118,
                           "height": 84},
                          "right1": {
                           "path": "73_R_P_C_1.png",
                           "width": 118,
                           "height": 84},
                          "right2": {
                           "path": "73_R_P_C_2.png",
                           "width": 118,
                           "height": 84},
                          "left_smoke1": {
                           "path": "73_L_P_S_1.png",
                           "width": 118,
                           "height": 84},
                          "left_smoke2": {
                           "path": "73_L_P_S_2.png",
                           "width": 118,
                           "height": 84},
                          "right_smoke1": {
                           "path": "73_R_P_S_1.png",
                           "width": 118,
                           "height": 84},
                          "right_smoke2": {
                           "path": "73_R_P_S_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_straight1": {
                           "path": "73_S_U_C_1.png",
                           "width": 100,
                           "height": 84},
                          "uphill_straight2": {
                           "path": "73_S_U_C_2.png",
                           "width": 100,
                           "height": 84},
                          "uphill_left1": {
                           "path": "73_L_U_C_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_left2": {
                           "path": "73_L_U_C_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right1": {
                           "path": "73_R_U_C_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right2": {
                           "path": "73_R_U_C_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_left_smoke1": {
                           "path": "73_L_U_S_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_left_smoke2": {
                           "path": "73_L_U_S_2.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right_smoke1": {
                           "path": "73_R_U_S_1.png",
                           "width": 118,
                           "height": 84},
                          "uphill_right_smoke2": {
                           "path": "73_R_U_S_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_straight1": {
                           "path": "73_S_D_C_1.png",
                           "width": 100,
                           "height": 84},
                          "downhill_straight2": {
                           "path": "73_S_D_C_2.png",
                           "width": 100,
                           "height": 84},
                          "downhill_left1": {
                           "path": "73_L_D_C_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_left2": {
                           "path": "73_L_D_C_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right1": {
                           "path": "73_R_D_C_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right2": {
                           "path": "73_R_D_C_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_left_smoke1": {
                           "path": "73_L_D_S_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_left_smoke2": {
                           "path": "73_L_D_S_2.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right_smoke1": {
                           "path": "73_R_D_S_1.png",
                           "width": 118,
                           "height": 84},
                          "downhill_right_smoke2": {
                           "path": "73_R_D_S_2.png",
                           "width": 118,
                           "height": 84}}},
                           ]

SPRITES           = {"column": {
                       "path": "column.png",
                       "collision": [0.05, 0.05],
                       "width": 90,
                       "height": 126},
                     "tunnel_entrance": {
                       "width": 80,
                       "height": 10,
                       "path": None,
                       "collision": [0, 0]},
                     "tunnel_light": {
                       "path": "tunnel_light.png",
                       "width": 8,
                       "height": 8},
                     "tunnel_sign": {
                       "path": "bush1.png",
                       "width": 20,
                       "height": 20},
                     "over_column": {
                       "path": "over_column.png",
                       "width": 480,
                       "height": 40},
                     "boat_house": {
                       "path": "boat_house.png",
                       "collision": [0.05, 0.01],
                       "width": 123,
                       "height": 128},
                     "bush1": {
                       "path": "bush3.png",
                       "collision": [0.4, 0.4],
                       "width": 64,
                       "height": 32},
                     "bush2": {
                       "path": "bush2.png",
                       "collision": [0.4, 0.4],
                       "width": 64,
                       "height": 32},
                     "palm_tree": {
                       "path": "palm-tree2.png",
                       "collision": [0.6, 0.1],
                       "width": 128,
                       "height": 256},
                     "tree1": {
                       "path": "tree2.png",
                       "collision": [0.64, 0.1],
                       "width": 128,
                       "height": 256},
                     "billboard1": {
                       "path": "billboard01.png",
                       "collision": [0.2, 0.2],
                       "width": 157,
                       "height": 128},
                     "billboard2": {
                       "path": "billboard02.png",
                       "collision": [0.05, 0.05],
                       "width": 155,
                       "height": 130},
                     "billboard3": {
                       "path": "billboard03.png",
                       "collision": [0.05, 0.05],
                       "width": 155,
                       "height": 130},
                     "billboard4": {
                       "path": "billboard04.png",
                       "collision": [0.05, 0.05],
                       "width": 155,
                       "height": 155},
                     "start": {
                       "path": "gate_start.png",
                       "width": 630,
                       "height": 128},
                     "gate_01": {
                       "path": "gate_01.png",
                       "width": 630,
                       "height": 128},
                     "gate_02": {
                       "path": "gate_02.png",
                       "width": 630,
                       "height": 128},
                     "gate_03": {
                       "path": "gate_03.png",
                       "width": 630,
                       "height": 128},
                     "boulder1": {
                       "path": "boulder2.png",
                       "collision": [0, 0],
                       "width": 64,
                       "height": 64},
                     "post": {
                       "path": "post.png",
                       "collision": [0.25, 0.25],
                       "width": 30,
                       "height": 56},
                     "light_post1": {
                       "path": "light_post1.png",
                       "width": 40,
                       "height": 90},
                     "light_post2": {
                       "path": "light_post2.png",
                       "width": 40,
                       "height": 90},
                     "left_sign": {
                       "path": "left_sign.png",
                       "width": 40,
                       "height": 90},
                     "right_sign": {
                       "path": "right_sign.png",
                       "width": 40,
                       "height": 90},
                     "traffic_light": {
                       "path": "traffic_light.png",
                       "width": 40,
                       "height": 90},
                     "competitor1": {
                       "path": "competitor1.png",
                       "collision": [0.05, 0.05],
                       "width": 90,
                       "height": 81},
                     "competitor2": {
                       "path": "competitor2.png",
                       "collision": [0.05, 0.05],
                       "width": 100,
                       "height": 84},
                     "competitor3": {
                       "path": "competitor3.png",
                       "collision": [0.05, 0.05],
                       "width": 100,
                       "height": 84},
                     "bonus": {
                       "path": "bonus.png",
                       "collision": [0, 0],
                       "bonus": True,
                       "width": 25,
                       "height": 25},
                     "speed_boost": {
                       "path": None,
                       "collision": [0, 0],
                       "speed_boost": True,
                       "width": 72,
                       "height": 42},
                     "hooker1": {
                       "path": "hooker1.png",
                       "collision": [0.42, 0.36],
                       "hooker": True,
                       "width": 25,
                       "height": 42},
                     "hooker2": {
                       "path": "hooker2.png",
                       "collision": [0.42, 0.36],
                       "hooker": True,
                       "width": 25,
                       "height": 42},
                     "hooker3": {
                       "path": "hooker3.png",
                       "collision": [0.42, 0.36],
                       "hooker": True,
                       "width": 25,
                       "height": 42},
                     "barrier": {
                       "path": "barrier.png",
                       "collision": [0.05, 0.05],
                       "width": 60,
                       "height": 35},
                     "house_01": {
                       "path": "house_01.png",
                       "width": 355,
                       "height": 256},
                     "house_02": {
                       "path": "house_02.png",
                       "width": 358,
                       "height": 258},
                     "house_03": {
                       "path": "house_03.png",
                       "width": 373,
                       "height": 190},
                     "house_04": {
                       "path": "house_04.png",
                       "width": 373,
                       "height": 190},
                     "house_05": {
                       "path": "house_05.png",
                       "width": 507,
                       "height": 249},
                     "house_06": {
                       "path": "house_06.png",
                       "width": 507,
                       "height": 249},
                     "house_07": {
                       "path": "house_07.png",
                       "width": 496,
                       "height": 357},
                     "house_08": {
                       "path": "house_08.png",
                       "width": 420,
                       "height": 358},
                     "house_09": {
                       "path": "house_09.png",
                       "width": 420,
                       "height": 358},
                     "house_10": {
                       "path": "house_10.png",
                       "width": 420,
                       "height": 358},
                     "house_11": {
                       "path": "house_11.png",
                       "width": 420,
                       "height": 358},
                     "house_1": {
                       "path": "house_1.png",
                       "collision": [0.05, 0.05],
                       "width": 249,
                       "height": 256},
                     "house_1_sm": {
                       "path": "house_1_sm.png",
                       "width": 123,
                       "height": 126},
                     "house_2_sm": {
                       "path": "house_2_sm.png",
                       "width": 174,
                       "height": 126},
                     "house_3_sm": {
                       "path": "house_3_sm.png",
                       "width": 173,
                       "height": 124},
                     "house_5_sm": {
                       "path": "house_5_sm.png",
                       "width": 254,
                       "height": 124},
                     "house_8_sm": {
                       "path": "house_8_sm.png",
                       "width": 210,
                       "height": 179},
                     "house_9_sm": {
                       "path": "house_9_sm.png",
                       "width": 210,
                       "height": 179},
                     "house_10_sm": {
                       "path": "house_10_sm.png",
                       "width": 210,
                       "height": 179},
                     "house_11_sm": {
                       "path": "house_11_sm.png",
                       "width": 210,
                       "height": 179},
                     "tree_01": {
                       "path": "tree_01.png",
                       "collision": [0.05, 0.05],
                       "width": 128,
                       "height": 256},
                     "tree_01_sm": {
                       "path": "tree_01_sm.png",
                       "collision": [0.05, 0.05],
                       "width": 128/2,
                       "height": 256/2},
                     "tree_02": {
                       "path": "tree_02.png",
                       "collision": [0.05, 0.05],
                       "width": 170,
                       "height": 256},
                     "tree_02_sm": {
                       "path": "tree_02_sm.png",
                       "collision": [0.05, 0.05],
                       "width": 170/2,
                       "height": 256/2},
                     "tree_03": {
                       "path": "tree_03.png",
                       "collision": [0.05, 0.05],
                       "width": 120,
                       "height": 240},
                     "tree_04": {
                       "path": "tree_04.png",
                       "collision": [0.05, 0.05],
                       "width": 140,
                       "height": 256},
                     "bush_01": {
                       "path": "bush_01.png",
                       "collision": [0.05, 0.05],
                       "width": 96,
                       "height": 62},
                     "bush_02": {
                       "path": "bush_02.png",
                       "collision": [0.05, 0.05],
                       "width": 96,
                       "height": 62},
                     "bush_03": {
                       "path": "bush_03.png",
                       "collision": [0.05, 0.05],
                       "width": 96,
                       "height": 62},
                     "bush_04": {
                       "path": "bush_04.png",
                       "collision": [0.05, 0.05],
                       "width": 96,
                       "height": 62},
                     "road_pile1": {
                       "path": "road_pile1.png",
                       "collision": [0.0, 0.0],
                       "width": 12,
                       "height": 42},
                     "road_pile2": {
                       "path": "road_pile2.png",
                       "collision": [0, 0],
                       "width": 12,
                       "height": 42},
                     "road_barrel1": {
                       "path": "road_barrel1.png",
                       "collision": [0.05, 0.05],
                       "width": 67/3,
                       "height": 99/3},
                     "post_01": {
                       "path": "post_01.png",
                       "collision": [0.05, 0.05],
                       "width": 100,
                       "height": 254},
                     "post_02": {
                       "path": "post_02.png",
                       "collision": [0.05, 0.05],
                       "width": 107,
                       "height": 254},
                     "post_03": {
                       "path": "post_03.png",
                       "collision": [0.05, 0.05],
                       "width": 100,
                       "height": 254},
                     "post_04": {
                       "path": "post_04.png",
                       "collision": [0.05, 0.05],
                       "width": 161,
                       "height": 254},
                     "post_06": {
                       "path": "post_06.png",
                       "collision": [0.05, 0.05],
                       "width": 95,
                       "height": 252},
                     "post_07": {
                       "path": "post_07.png",
                       "collision": [0.05, 0.05],
                       "width": 95,
                       "height": 252},
                     "gate_05": {
                       "path": "gate_05.png",
                       "width": 630,
                       "height": 183},
                     "gate_06": {
                       "path": "gate_06.png",
                       "width": 630,
                       "height": 183},
                     "gate_07": {
                       "path": "gate_07.png",
                       "width": 630,
                       "height": 183},
                     "gate_08": {
                       "path": "gate_08.png",
                       "width": 630,
                       "height": 183},
                     "board_left_01": {
                       "path": "board_left_01.png",
                       "width": 75,
                       "height": 45},
                     "tractor_blue": {
                       "path": "tractor_blue.png",
                       "width": 350/2,
                       "height": 188/2},
                     "tractor_yellow": {
                       "path": "tractor_yellow.png",
                       "width": 350/2,
                       "height": 188/2},
                     "tractor_red": {
                       "path": "tractor_red.png",
                       "width": 774/2,
                       "height": 192/2},
                     "tractor_green": {
                       "path": "tractor_green.png",
                       "width": 583/2,
                       "height": 214/2},
                     "Ship_1": {
                       "path": "Ship_1.png",
                       "width": 600/2,
                       "height": 230/2},
                     "Ship_2": {
                       "path": "Ship_2.png",
                       "width": 600/2,
                       "height": 130/2},
                     "Ship_3": {
                       "path": "Ship_3.png",
                       "width": 600/2,
                       "height": 444/2},
                     "Ship_4": {
                       "path": "Ship_4.png",
                       "width": 600/2,
                       "height": 444/2},
                     "Ship_5": {
                       "path": "Ship_5.png",
                       "width": 600/2,
                       "height": 171/2}
                     }

if os.path.isfile("swervin_mervin/settings_local.py"):
    exec(open("swervin_mervin/settings_local.py").read())
    #execfile("swervin_mervin/settings_local.py")

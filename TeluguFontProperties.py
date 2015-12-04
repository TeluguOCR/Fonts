#! /usr/bin/env python

# File contains the properties of available Telugu Fonts
# Font Name 
# Style of gho (Kannada/Telugu) 
# Style of repha (Bottom/Left/Right) 
# Special form for ppu 
# Required Letter Spacing (Single/Double) ## Not used right now
# Nice Abbreviation
# Has Bold?

SIZE, GHO, REPHA, PPU, SPACING, ABBR, BOLD = range(7)
FP_DICT = { \
'Akshar Unicode':       	[48, 'K', 'BB', 0, 1, 'Akshar', 1],			\
#'AV-Web-Tel1':	     		[48, 'K', 'BB', 0, 1, 'AVWeb', 1],  	=LOHIT		\
'Dhurjati':		       	    [48, 'K', 'BB', 0, 1, 'Dhurjati', 1],			\
#'DKM Telugu':	      		[48, 'K', 'BB', 0, 1, 'DKM', 1],		=LOHIT	    \
'Gautami':		        	[48, 'K', 'BB', 0, 1, 'Gautami', 1],			\
'Gidugu':		     	    [48, 'K', 'BR', 1, 1, 'Gidugu', 1],			\
'GIST-TLOTAmma':			[28, 'K', 'LR', 1, 1, 'Amma', 1],			    \
'GIST-TLOTAmruta':			[28, 'K', 'LR', 1, 1, 'Amruta', 0],			\
'GIST-TLOTAtreya':			[28, 'K', 'LR', 1, 1, 'Atreya', 1],			\
'GIST-TLOTChandana':		[28, 'K', 'LR', 1, 1, 'Chandana', 0],			\
'GIST-TLOTDeva':			[28, 'K', 'LR', 1, 1, 'Deva', 1],			    \
'GIST-TLOTDraupadi':		[28, 'K', 'LR', 1, 1, 'Draupadi', 1],			\
'GIST-TLOTGolkonda':		[28, 'K', 'LR', 1, 1, 'Golkonda', 0],			\
'GIST-TLOTKrishna':			[28, 'K', 'LR', 1, 1, 'Krishna', 1],			\
#'GIST-TLOTManu':			[28, 'K', 'LR', 1, 1, 'Manu', 1],			    \
'GIST-TLOTMenaka':			[28, 'K', 'LR', 1, 1, 'Menaka', 1],			\
'GIST-TLOTPavani':			[28, 'K', 'LR', 1, 1, 'Pavani', 0],			\
'GIST-TLOTPriya':			[22, 'K', 'LR', 1, 1, 'Priya', 0],			    \
#'GIST-TLOTRajan':			[28, 'K', 'LR', 1, 1, 'Rajan', 1],			    \
'GIST-TLOTRajani':			[28, 'K', 'LR', 1, 1, 'Rajani', 0],			\
'GIST-TLOTSanjana':			[28, 'K', 'LR', 1, 1, 'Sanjana', 0],			\
'GIST-TLOTSitara':			[28, 'K', 'LR', 1, 1, 'Sitara', 0],			\
'GIST-TLOTSwami':			[28, 'K', 'LR', 1, 1, 'Swami', 0],			    \
'GIST-TLOTVennela':			[28, 'K', 'LR', 1, 1, 'Vennela', 1],			\
'Gurajada':			        [48, 'K', 'BR', 1, 1, 'Gurajada', 1],			\
'LakkiReddy':	            [48, 'K', 'BB', 0, 1, 'LakkiReddy', 1],		\
'Lohit Telugu':	            [48, 'K', 'BB', 0, 1, 'Lohit', 1],			    \
'Mallanna':		            [48, 'T', 'BB', 0, 1, 'Mallanna', 1],			\
'Mandali':		            [48, 'T', 'LB', 0, 1, 'Mandali', 1],			\
'Nandini':		            [48, 'K', 'LL', 0, 1, 'Nandini', 1],			\
'NATS':			            [48, 'K', 'BR', 1, 1, 'NATS', 1],			    \
'NTR':			            [48, 'K', 'BB', 1, 1, 'NTR', 1],			    \
'Peddana':		            [48, 'K', 'BR', 0, 1, 'Peddana', 1],			\
'Ponnala':		            [48, 'K', 'BB', 0, 1, 'Ponnala', 1],			\
'Pothana2000':	            [48, 'K', 'BR', 1, 1, 'Pothana', 1],			\
'Ramabhadra1':	            [48, 'T', 'BB', 0, 1, 'Ramabhadra', 1],		\
'RamaneeyaWin':	            [48, 'K', 'BB', 0, 1, 'Ramaneeya', 1],			\
'Ramaraja':		            [48, 'K', 'BB', 0, 1, 'Ramaraja', 1],			\
'RaviPrakash':	            [48, 'K', 'BB', 0, 1, 'RaviPrakash', 1],		\
'Sree Krushnadevaraya':  	[48, 'T', 'BB', 0, 1, 'Krushnadeva', 1],		\
'Subhadra':			        [48, 'T', 'BB', 0, 1, 'Subhadra', 1],			\
'Suguna':			        [48, 'T', 'BB', 1, 2, 'Suguna', 1],			\
'Suranna':			        [48, 'T', 'LBR', 0, 1, 'Suranna', 1],			\
'SuraVara_Samhita':	        [48, 'K', 'BB', 0, 1, 'Samhita', 1],			\
'SURAVARA_Swarna':	        [48, 'K', 'BB', 0, 1, 'Swarna', 1],	 		\
'Suravaram':		        [48, 'K', 'BR', 1, 1, 'Suravaram', 1],			\
'TenaliRamakrishna':        [48, 'K', 'BB', 0, 1, 'Tenali', 1],			\
'Timmana':			        [48, 'K', 'BB', 0, 1, 'Timmana', 0],			\
#'TLW-TTHemalatha':	        [48, 'K', 'BB', 0, 1, 'Hemalatha', 1],	=LOHIT		\
'Vajram':                   [48, 'K', 'BB', 0, 1, 'Vajram', 1],         \
'Vani':                   [48, 'K', 'BR', 0, 1, 'Vani', 1],         \
'Vemana2000':		        [48, 'K', 'BR', 1, 1, 'Vemana', 1] 			\
}

if __name__ == '__main__':
    import cairo
    import pango
    import pangocairo

    #get font families:
    font_map = pangocairo.cairo_font_map_get_default()
    families = font_map.list_families()
    font_names = [f.get_name() for f in families]
    for f in sorted(font_names):
        print (f)


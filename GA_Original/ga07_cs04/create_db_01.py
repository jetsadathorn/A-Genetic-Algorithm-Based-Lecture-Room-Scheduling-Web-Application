import sqlite3 as sql
conn = sql.connect('class_schedule.db')
c = conn.cursor()
c.execute("""create table room (number text, capacity integer)""")
c.execute("insert into room Values ('R1', 20),"
                                  "('R2', 30),"
		  						  "('R3', 25)")
c.execute("""create table course (number text, name text, max_numb_of_students, numb_of_sessions)""")
c.execute("insert into course Values ('C1', '408C', 20, 1),"
									"('C2', '302',  25, 1),"
									"('C3', '427J', 20, 2),"
									"('C4', '411',  25, 1),"
									"('C5', '306',  25, 1),"
									"('C6', '319K', 25, 1),"
									"('C7', '312',  30, 1),"
									"('C8', '303L', 30, 1),"
									"('C9', '340L', 30, 1)")
c.execute("""create table meeting_time (id text, time text)""")
c.execute("insert into meeting_time Values ('MT1', 'MWF 08:00 - 09:00'),"
                                          "('MT2', 'MWF 09:00 - 10:00'),"
		                                  "('MT3', 'MWF 10:00 - 11:00'),"
                                          "('MT4', 'TTH 08:00 - 09:30'),"
		                                  "('MT5', 'TTH 09:30 - 11:00'),"
                                          "('MT6', 'TTH 11:00 - 12:30')")
c.execute("""create table instructor (number text, name text)""")
c.execute("insert into instructor Values ('I1', 'Dr. A. Bluebery'),"
                      					"('I2', 'Mr. B. Blackbery'),"
                      					"('I3', 'Dr. D. Raspbery'),"
                    					"('I4', 'Mr. B. Strawbery'),"
                      					"('I5', 'Dr. D. Bilbery'),"
                      					"('I6', 'Mrs M. Cranbery'),"
                      					"('I7', 'Dr. A. Whitebery')")
c.execute("""create table dept_instructor (dept_name text, instructor_id text)""")
c.execute("insert into dept_instructor Values ('MATH', 'I1'),"
									         "('MATH', 'I2'),"
									         "('EE',   'I3'),"
									    	 "('EE',   'I4'),"
									    	 "('EE',   'I5'),"
		                                     "('PHY',  'I6'),"
									    	 "('MATH', 'I7')")
c.execute("""create table instructor_availability (instructor_id text, meeting_time_id text)""")
c.execute("insert into instructor_availability(instructor_id, meeting_time_id) values "
                                                   "('I1', 'MT1'),"
									               "('I1', 'MT2'),"
									               "('I1', 'MT3'),"
									               "('I1', 'MT4'),"	
									               "('I1', 'MT5'),"
									               "('I1', 'MT6'),"	
									               
									    		   "('I2', 'MT2'),"
									    		   "('I2', 'MT3'),"
									    		   "('I2', 'MT4'),"
									    		   "('I2', 'MT5'),"
									    		   "('I2', 'MT6'),"
									    		  
									    		   "('I3', 'MT1'),"
									    		   "('I3', 'MT2'),"
									    		   "('I3', 'MT3'),"
									    		   "('I3', 'MT4'),"
									    		   "('I3', 'MT5'),"
									    		   "('I3', 'MT6'),"
												   "('I4', 'MT1'),"
												   "('I4', 'MT2'),"
												   "('I4', 'MT3'),"
											       "('I4', 'MT4'),"
												   "('I4', 'MT5'),"
												   "('I4', 'MT6'),"
												   "('I5', 'MT1'),"
												   "('I5', 'MT2'),"
												   "('I5', 'MT3'),"
												   "('I5', 'MT4'),"
												   "('I5', 'MT5'),"
												   "('I5', 'MT6'),"   
												  
												   "('I6', 'MT1'),"
												   "('I6', 'MT2'),"
												   "('I6', 'MT3'),"
												   "('I6', 'MT4'),"
												   "('I6', 'MT5'),"
									    		   "('I6', 'MT6'),"  
									    		   "('I7', 'MT1'),"
												   "('I7', 'MT2'),"
												   "('I7', 'MT3'),"
												   "('I7', 'MT4'),"
												   "('I7', 'MT5'),"
												   "('I7', 'MT6')")
c.execute("""create table course_instructor (course_number text, instructor_number text)""")
c.execute("insert into course_instructor Values  ('C1', 'I1'),"
												"('C1', 'I2'),"
												"('C1', 'I7'),"
												"('C2', 'I3'),"
												"('C2', 'I4'),"
												"('C2', 'I5'),"
												"('C3', 'I1'),"
												"('C3', 'I2')," 
												"('C4', 'I3'),"
												"('C4', 'I4'),"
												"('C4', 'I5'),"
												"('C5', 'I3'),"
												"('C5', 'I4'),"
												"('C5', 'I5'),"
												"('C6', 'I3'),"
												"('C6', 'I4'),"
												"('C6', 'I5'),"
												"('C7', 'I3'),"
												"('C7', 'I4'),"
												"('C7', 'I5'),"
												"('C8', 'I6'),"
												"('C9', 'I1'),"
												"('C9', 'I2'),"
												"('C9', 'I7')")
c.execute("""create table dept (name text)""")
c.execute("insert into dept Values ('MATH'),"
                                  "('EE'),"
                                  "('PHY')")
c.execute("""create table dept_course (name text, course_numb text)""")
c.execute("insert into dept_course Values ('MATH', 'C1'),"
									     "('EE',   'C2'),"
									     "('MATH', 'C3'),"
									     "('EE',   'C4'),"
									     "('EE',   'C5'),"
									     "('EE',   'C6'),"
									     "('EE',   'C7'),"
									     "('PHY',  'C8'),"
									     "('MATH', 'C9')")
c.execute("""create table student (number text, name text, status text)""")
c.execute("insert into student Values('S001', 'A. Oregano',    'FT'),"
                      "('S002', 'B. Thyme',      'FT'),"
                      "('S003', 'C. Basil',      'FT'),"
                      "('S004', 'D. Pine',       'FT'),"
                      "('S005', 'A. Olive',      'FT'),"
                      "('S006', 'F. Lime',       'FT'),"
                      "('S007', 'T. peppermint', 'FT'),"
                      "('S008', 'W. Vanilla',    'FT'),"
                      "('S009', 'I. Basil',      'FT'),"
                      "('S010', 'J. Cacao',      'PT'),"
                      "('S011', 'M. Walnut',     'FT'),"
                      "('S012', 'N. Pecans',     'FT'),"
                      "('S013', 'P. Hazelnuts',  'FT'),"
                      "('S014', 'K. Cashews',    'FT'),"
                      "('S015', 'L. Peanuts',    'FT'),"
                      "('S016', 'S. Almonds',    'PT'),"
                      "('S017', 'K. Pistachios', 'FT'),"
                      "('S018', 'B. Macadamia',  'FT'),"
                      "('S019', 'D. grapes',     'PT'),"
                      "('S020', 'G. butternuts', 'FT'),"
                      "('S021', 'A. Robin',      'FT'),"
                      "('S022', 'B. BlueJay',    'FT'),"
                      "('S023', 'C. StellerJay', 'FT'),"
                      "('S024', 'D. Crow',       'PT'),"
                      "('S025', 'A. Mockingbird','FT'),"
                      "('S026', 'F. Starling',   'FT'),"
                      "('S027', 'T. Magpie',     'FT'),"
                      "('S028', 'W. Junco',      'FT'),"
                      "('S029', 'I. Sparrow',    'FT'),"
                      "('S030', 'J. Goldfinch',  'FT'),"
                      "('S031', 'A. Woodpecker', 'FT'),"
                      "('S032', 'B. Flamingo',   'FT'),"
                      "('S033', 'C. Stork',      'FT'),"
                      "('S034', 'D. Gull',       'FT'),"
                      "('S035', 'A. Shrikes',    'FT'),"
                      "('S036', 'F. Chukar',     'FT'),"
                      "('S037', 'T. Stock',      'FT'),"
                      "('S038', 'W. Deer',       'FT'),"
                      "('S039', 'I. Fox',        'FT'),"
                      "('S040', 'J. Wolf',       'FT'),"
                      "('S041', 'A. Jackal',     'FT'),"
                      "('S042', 'B. Eagle',      'FT'),"
                      "('S043', 'C. Caracal',    'FT'),"
                      "('S044', 'D. Gazelle',    'FT'),"
                      "('S045', 'A. Finch',      'FT'),"
                      "('S046', 'F. Parrot',     'FT'),"
                      "('S047', 'T. Cockatoo',   'FT'),"
                      "('S048', 'W. Honeyeater', 'FT'),"
                      "('S049', 'I. Galah',      'FT'),"
                      "('S050', 'J. Emu',        'FT')")
c.execute("""create table student_availability (student_id text, meeting_time_id text)""")
c.execute("insert into student_availability(student_id, meeting_time_id) values "
                                                     "('S001', 'MT1'),"
									                 "('S001', 'MT2'),"				
									    		     "('S001', 'MT3'),"
									    		     "('S001', 'MT4'),"
									    		     "('S001', 'MT5'),"
									                 "('S001', 'MT6'),"				
									    	
													 "('S002', 'MT1'),"
													 "('S002', 'MT2'),"				
													 "('S002', 'MT3'),"
													 "('S002', 'MT4'),"
													 "('S002', 'MT5'),"
									                 "('S002', 'MT6'),"				
													 
													 "('S003', 'MT1'),"
													 "('S003', 'MT2'),"				
													 "('S003', 'MT3'),"
													 "('S003', 'MT4'),"
													 "('S003', 'MT5'),"
													 "('S003', 'MT6'),"

													 "('S004', 'MT1'),"
													 "('S004', 'MT2'),"
													 "('S004', 'MT3'),"
													 "('S004', 'MT4'),"
													 "('S004', 'MT5'),"
		                                             "('S004', 'MT6'),"

													 "('S005', 'MT1'),"
													 "('S005', 'MT2'),"
													 "('S005', 'MT3'),"
													 "('S005', 'MT4'),"
													 "('S005', 'MT5'),"
													 "('S005', 'MT6'),"

													 "('S006', 'MT1'),"
													 "('S006', 'MT2'),"
													 "('S006', 'MT3'),"
													 "('S006', 'MT4'),"
													 "('S006', 'MT5'),"
													 "('S006', 'MT6'),"

													 "('S007', 'MT1'),"
													 "('S007', 'MT2'),"
													 "('S007', 'MT3'),"
													 "('S007', 'MT4'),"
													 "('S007', 'MT5'),"
													 "('S007', 'MT6'),"

													 "('S008', 'MT1'),"
													 "('S008', 'MT2'),"
													 "('S008', 'MT3'),"
													 "('S008', 'MT4'),"
													 "('S008', 'MT5'),"
													 "('S008', 'MT6'),"

													 "('S009', 'MT1'),"
													 "('S009', 'MT2'),"
													 "('S009', 'MT3'),"
													 "('S009', 'MT4'),"
													 "('S009', 'MT5'),"
													 "('S009', 'MT6'),"

													 "('S010', 'MT1'),"
													 "('S010', 'MT2'),"
													 "('S010', 'MT3'),"
													 "('S010', 'MT4'),"
													 "('S010', 'MT5'),"
													 "('S010', 'MT6'),"

													"('S011', 'MT1'),"
													"('S011', 'MT2'),"
													"('S011', 'MT3'),"
													"('S011', 'MT4'),"
													"('S011', 'MT5'),"
													"('S011', 'MT6'),"

													"('S012', 'MT1'),"
													"('S012', 'MT2'),"
													"('S012', 'MT3'),"
													"('S012', 'MT4'),"
													"('S012', 'MT5'),"
													"('S012', 'MT6'),"

													"('S013', 'MT1'),"
													"('S013', 'MT2'),"
													"('S013', 'MT3'),"
													"('S013', 'MT4'),"
													"('S013', 'MT5'),"
													"('S013', 'MT6'),"

													"('S014', 'MT1'),"
													"('S014', 'MT2'),"
													"('S014', 'MT3'),"
													"('S014', 'MT4'),"
													"('S014', 'MT5'),"
													"('S014', 'MT6'),"


													"('S015', 'MT1'),"
													"('S015', 'MT2'),"
													"('S015', 'MT3'),"
													"('S015', 'MT4'),"
													"('S015', 'MT5'),"
													"('S015', 'MT6'),"

													"('S016', 'MT1'),"
													"('S016', 'MT2'),"
													"('S016', 'MT3'),"
													"('S016', 'MT4'),"
													"('S016', 'MT5'),"
													"('S016', 'MT6'),"

													"('S017', 'MT1'),"
													"('S017', 'MT2'),"
													"('S017', 'MT3'),"
													"('S017', 'MT4'),"
													"('S017', 'MT5'),"
													"('S017', 'MT6'),"

													"('S018', 'MT1'),"
													"('S018', 'MT2'),"
													"('S018', 'MT3'),"
													"('S018', 'MT4'),"
													"('S018', 'MT5'),"
													"('S018', 'MT6'),"

													"('S019', 'MT1'),"
													"('S019', 'MT2'),"
													"('S019', 'MT3'),"
													"('S019', 'MT4'),"
													"('S019', 'MT5'),"
													"('S019', 'MT6'),"

													"('S020', 'MT1'),"
													"('S020', 'MT2'),"
													"('S020', 'MT3'),"
													"('S020', 'MT4'),"
									    		    "('S020', 'MT5'),"
									                "('S020', 'MT6'),"


									    		    "('S021', 'MT1'),"
									    		    "('S021', 'MT2'),"
									    		    "('S021', 'MT3'),"
									    		    "('S021', 'MT4'),"
									    		    "('S021', 'MT5'),"
									    		    "('S021', 'MT6'),"

									    		    "('S022', 'MT1'),"
									    		    "('S022', 'MT2'),"
									    		    "('S022', 'MT3'),"
									    		    "('S022', 'MT4'),"
									    		    "('S022', 'MT5'),"
									    		    "('S022', 'MT6'),"

									    		    "('S023', 'MT1'),"
									    		    "('S023', 'MT2'),"
									    		    "('S023', 'MT3'),"
									    		    "('S023', 'MT4'),"
									    		    "('S023', 'MT5'),"
									    		    "('S023', 'MT6'),"

									    		    "('S024', 'MT1'),"
									    		    "('S024', 'MT2'),"
									    		    "('S024', 'MT3'),"
									    		    "('S024', 'MT4'),"
									    		    "('S024', 'MT5'),"
									    		    "('S024', 'MT6'),"

									    		    "('S025', 'MT1'),"
									    		    "('S025', 'MT2'),"
									    		    "('S025', 'MT3'),"
									    		    "('S025', 'MT4'),"
									    		    "('S025', 'MT5'),"
									    		    "('S025', 'MT6'),"

									    		    "('S026', 'MT1'),"
									    		    "('S026', 'MT2'),"
									    		    "('S026', 'MT3'),"
									    		    "('S026', 'MT4'),"
									    		    "('S026', 'MT5'),"
									    		    "('S026', 'MT6'),"

									    		    "('S027', 'MT1'),"
									    		    "('S027', 'MT2'),"
									    		    "('S027', 'MT3'),"
									    		    "('S027', 'MT4'),"
									    		    "('S027', 'MT5'),"
									    		    "('S027', 'MT6'),"

									    		    "('S028', 'MT1'),"
									    		    "('S028', 'MT2'),"
									    		    "('S028', 'MT3'),"
									    		    "('S028', 'MT4'),"
									    		    "('S028', 'MT5'),"
									    		    "('S028', 'MT6'),"

									    		    "('S029', 'MT1'),"
									    		    "('S029', 'MT2'),"
									    		    "('S029', 'MT3'),"
									    		    "('S029', 'MT4'),"
									    		    "('S029', 'MT5'),"
									    		    "('S029', 'MT6'),"

									    		    "('S030', 'MT1'),"
									    		    "('S030', 'MT2'),"
									    		    "('S030', 'MT3'),"
									    		    "('S030', 'MT4'),"
									    		    "('S030', 'MT5'),"
									    		    "('S030', 'MT6'),"

									    		    "('S031', 'MT1'),"
									    		    "('S031', 'MT2'),"
									    		    "('S031', 'MT3'),"
									    		    "('S031', 'MT4'),"
									    		    "('S031', 'MT5'),"
									    		    "('S031', 'MT6'),"

									    		    "('S032', 'MT1'),"
									    		    "('S032', 'MT2'),"
									    		    "('S032', 'MT3'),"
									    		    "('S032', 'MT4'),"
									    		    "('S032', 'MT5'),"
									    		    "('S032', 'MT6'),"

									    		    "('S033', 'MT1'),"
									    		    "('S033', 'MT2'),"
									    		    "('S033', 'MT3'),"
									    		    "('S033', 'MT4'),"
									    		    "('S033', 'MT5'),"
									    		    "('S033', 'MT6'),"

									    		    "('S034', 'MT1'),"
									    		    "('S034', 'MT2'),"
									    		    "('S034', 'MT3'),"
									    		    "('S034', 'MT4'),"
									    		    "('S034', 'MT5'),"
									    		    "('S034', 'MT6'),"

									    		    "('S035', 'MT1'),"
									    		    "('S035', 'MT2'),"
									    		    "('S035', 'MT3'),"
									    		    "('S035', 'MT4'),"
									    		    "('S035', 'MT5'),"
									    		    "('S035', 'MT6'),"

									    		    "('S036', 'MT1'),"
									    		    "('S036', 'MT2'),"
									    		    "('S036', 'MT3'),"
									    		    "('S036', 'MT4'),"
									    		    "('S036', 'MT5'),"
									    		    "('S036', 'MT6'),"

									    		    "('S037', 'MT1'),"
									    		    "('S037', 'MT2'),"
									    		    "('S037', 'MT3'),"
									    		    "('S037', 'MT4'),"
									    		    "('S037', 'MT5'),"
									    		    "('S037', 'MT6'),"

									    		    "('S038', 'MT1'),"
									    		    "('S038', 'MT2'),"
									    		    "('S038', 'MT3'),"
									    		    "('S038', 'MT4'),"
									    		    "('S038', 'MT5'),"
									    		    "('S038', 'MT6'),"

									    		    "('S039', 'MT1'),"
									    		    "('S039', 'MT2'),"
									    		    "('S039', 'MT3'),"
									    		    "('S039', 'MT4'),"
									    		    "('S039', 'MT5'),"
									    		    "('S039', 'MT6'),"

									    		    "('S040', 'MT1'),"
									    		    "('S040', 'MT2'),"
									    		    "('S040', 'MT3'),"
									    		    "('S040', 'MT4'),"
									    		    "('S040', 'MT5'),"
									    	        "('S040', 'MT6'),"

    										        "('S041', 'MT1'),"
    										        "('S041', 'MT2'),"
    										        "('S041', 'MT3'),"
    										        "('S041', 'MT4'),"
    										        "('S041', 'MT5'),"
    										        "('S041', 'MT6'),"

    										        "('S042', 'MT1'),"
    										        "('S042', 'MT2'),"
    										        "('S042', 'MT3'),"
    										        "('S042', 'MT4'),"
    									        	"('S042', 'MT5'),"
    										        "('S042', 'MT6'),"

    										        "('S043', 'MT1'),"
                                                    "('S043', 'MT2'),"
                                                    "('S043', 'MT3'),"
                                                    "('S043', 'MT4'),"
                                                    "('S043', 'MT5'),"
                                                    "('S043', 'MT6'),"

                                                    "('S044', 'MT1'),"
                                                    "('S044', 'MT2'),"
                                                    "('S044', 'MT3'),"
                                                    "('S044', 'MT4'),"
                                                    "('S044', 'MT5'),"
                                                    "('S044', 'MT6'),"

                                                    "('S045', 'MT1'),"
                                                    "('S045', 'MT2'),"
                                                    "('S045', 'MT3'),"
                                                    "('S045', 'MT4'),"
                                                    "('S045', 'MT5'),"
                                                    "('S045', 'MT6'),"

                                                    "('S046', 'MT1'),"
                                                    "('S046', 'MT2'),"
                                                    "('S046', 'MT3'),"
                                                    "('S046', 'MT4'),"
                                                    "('S046', 'MT5'),"
                                                    "('S046', 'MT6'),"

                                                    "('S047', 'MT1'),"
                                                    "('S047', 'MT2'),"
                                                    "('S047', 'MT3'),"
                                                    "('S047', 'MT4'),"
                                                    "('S047', 'MT5'),"
                                                    "('S047', 'MT6'),"

                                                    "('S048', 'MT1'),"
                                                    "('S048', 'MT2'),"
                                                    "('S048', 'MT3'),"
                                                    "('S048', 'MT4'),"
                                                    "('S048', 'MT5'),"
                                                    "('S048', 'MT6'),"

                                                    "('S049', 'MT1'),"
                                                    "('S049', 'MT2'),"
                                                    "('S049', 'MT3'),"
                                                    "('S049', 'MT4'),"
                                                    "('S049', 'MT5'),"
                                                    "('S049', 'MT6'),"

                                                    "('S050', 'MT1'),"
                                                    "('S050', 'MT2'),"
                                                    "('S050', 'MT3'),"
                                                    "('S050', 'MT4'),"
                                                    "('S050', 'MT5'),"
                                                    "('S050', 'MT6')")
c.execute("""CREATE TABLE course_prereqs (course_number text, prereq_course_number text)""")
c.execute("INSERT INTO course_prereqs Values ('C2', 'C1'),"
				                            "('C4', 'C1'),"
											"('C4', 'C2'),"
											"('C4', 'C3'),"	
											"('C4', 'C8'),"	
											"('C5', 'C1'),"
											"('C6', 'C1'),"
											"('C6', 'C5'),"
											"('C7', 'C1'),"
											"('C7', 'C5')")
c.execute("""CREATE TABLE courses_passed (student_id text, course_number text)""")
c.execute("INSERT INTO courses_passed Values ('S001', 'C1'),"
												         "('S001', 'C2'),"
												         "('S003', 'C1'),"
												         "('S004', 'C1'),"
												         "('S004', 'C2'),"
												         "('S004', 'C3'),"
												         "('S004', 'C4'),"
												         "('S005', 'C3'),"
												         "('S006', 'C3'),"
												         "('S007', 'C1'),"
												         "('S007', 'C5'),"
												         "('S008', 'C3'),"
												         "('S009', 'C8'),"
												         "('S010', 'C1'),"
														 "('S011', 'C1'),"
														 "('S011', 'C5'),"
														 "('S012', 'C1'),"
														 "('S012', 'C5'),"
														 "('S013', 'C1'),"
														 "('S013', 'C5'),"
														 "('S014', 'C1'),"
														 "('S014', 'C5'),"
														 "('S015', 'C1'),"
														 "('S015', 'C5'),"
														
														 "('S016', 'C1'),"
														 "('S016', 'C2'),"
														 "('S016', 'C3'),"
														 "('S016', 'C8'),"
														
														"('S017', 'C1'),"
														"('S017', 'C2'),"
														"('S017', 'C3'),"
														"('S017', 'C8'),"
														
														"('S018', 'C1'),"
														"('S018', 'C2'),"
														"('S018', 'C3'),"
														"('S018', 'C8'),"

														"('S019', 'C1'),"
														"('S019', 'C2'),"
														"('S019', 'C3'),"
														"('S019', 'C8'),"
														
														"('S020', 'C1'),"
														"('S020', 'C2'),"
														"('S020', 'C3'),"
														"('S020', 'C8'),"
														
														"('S021', 'C1'),"
														"('S021', 'C2'),"
														"('S021', 'C3'),"
														"('S021', 'C8'),"
														
														"('S022', 'C1'),"
														"('S022', 'C2'),"
														"('S022', 'C3'),"
														"('S022', 'C8'),"
														
														"('S023', 'C1'),"
														"('S023', 'C2'),"
														"('S023', 'C3'),"
														"('S023', 'C8'),"
														
														"('S024', 'C1'),"
														"('S024', 'C2'),"
														"('S024', 'C3'),"
														"('S024', 'C8'),"
														
														"('S025', 'C1'),"
														"('S025', 'C2'),"
														"('S025', 'C3'),"
														"('S025', 'C8'),"

														"('S026', 'C1'),"
														"('S026', 'C2'),"
														"('S026', 'C3'),"
														"('S026', 'C8'),"
														
														"('S027', 'C1'),"
														"('S027', 'C2'),"
														"('S027', 'C3'),"
														"('S027', 'C8'),"
														
														"('S028', 'C1'),"
														"('S029', 'C1'),"
														"('S030', 'C1'),"
														"('S031', 'C1'),"
														"('S032', 'C1'),"
														"('S033', 'C1'),"
														"('S034', 'C1'),"
														"('S035', 'C1'),"
														"('S036', 'C1'),"
														"('S037', 'C1')")
conn.commit()
c.close()
conn.close()
#add table dept_instructor
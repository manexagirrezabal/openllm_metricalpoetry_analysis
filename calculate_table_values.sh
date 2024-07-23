#Table 1:
#Row 1:
python3 analyze_nolines_withstar7b.py 4 #Complex=True
python3 analyze_nolines_withstar7b.py 4 #Complex=False
python3 analyze_nolines7b.py 7
python3 analyze_nolines7b.py 8
python3 analyze_nolines7b.py 14
#Row 2:
python3 analyze_nolines_withstar.py 4 #Complex=True
python3 analyze_nolines_withstar.py 4 #Complex=False
python3 analyze_nolines.py 7
python3 analyze_nolines.py 8
python3 analyze_nolines.py 14

#Table 2:
#Row 1:
python3 analyze_nolines7b.py 16 4-4-4-4
python3 analyze_nolines7b.py 12 3-3-3-3
python3 analyze_nolines7b.py 14 4-4-4-2
#Row 2:
python3 analyze_nolines.py 16 4-4-4-4
python3 analyze_nolines.py 12 3-3-3-3 #ERROR
python3 analyze_nolines.py 14 4-4-4-2

#Table 3:
#Row 1:
python3 analyze_nostanzas7b_accuracy.py 1
python3 analyze_nostanzas7b_accuracy.py 2
python3 analyze_nostanzaswithnolineswithstar7b_accuracy.py 4 #complex=False
python3 analyze_nostanzaswithnolineswithstar7b_accuracy.py 4 #complex=True
#Row 2
python3 analyze_nostanzas_accuracy.py 1
python3 analyze_nostanzas_accuracy.py 2
python3 analyze_nostanzaswithnolineswithstar_accuracy.py 4 #complex=False
python3 analyze_nostanzaswithnolineswithstar_accuracy.py 4 #complex=True

#Table 4:
#Row 1:
python3 analyze_nosyllables7b_accuracy.py 8
python3 analyze_nosyllables7b_accuracy.py 10
python3 analyze_nosyllables7b_accuracy.py 13
#Row 2:
python3 analyze_nosyllables_accuracy.py 8
python3 analyze_nosyllables_accuracy.py 10
python3 analyze_nosyllables_accuracy.py 13

#Table 5:
python3 analyze_group_interrouge7b.py
python3 analyze_group_interrouge.py




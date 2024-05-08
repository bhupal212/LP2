% https://swish.swi-prolog.org/
% Symptoms for Common Illnesses
symptom(cold, sneezing).
symptom(cold, runny_nose).
symptom(cold, sore_throat).
symptom(cold, cough).
symptom(cold, mild_fever).

symptom(flu, high_fever).
symptom(flu, body_aches).
symptom(flu, headache).
symptom(flu, dry_cough).
symptom(flu, sore_throat).

symptom(strep_throat, sore_throat).
symptom(strep_throat, swollen_lymph_nodes).
symptom(strep_throat, fever).
symptom(strep_throat, rash).

symptom(allergies, sneezing).
symptom(allergies, itchy_eyes).
symptom(allergies, runny_nose).
symptom(allergies, watery_eyes).

symptom(asthma, shortness_of_breath).
symptom(asthma, wheezing).
symptom(asthma, chest_tightness).
symptom(asthma, coughing).

symptom(pneumonia, high_fever).
symptom(pneumonia, chills).
symptom(pneumonia, difficulty_breathing).
symptom(pneumonia, chest_pain).
symptom(pneumonia, productive_cough).

symptom(ear_infection, ear_pain).
symptom(ear_infection, hearing_loss).
symptom(ear_infection, fever).
symptom(ear_infection, drainage_from_ear).

symptom(uti, frequent_urination).
symptom(uti, burning_sensation_during_urination).
symptom(uti, cloudy_urine).
symptom(uti, abdominal_pain).

symptom(gastroenteritis, diarrhea).
symptom(gastroenteritis, abdominal_pain).
symptom(gastroenteritis, nausea).
symptom(gastroenteritis, vomiting).

% Function for diagnoses:
diagnose(Illness, Symptoms) :-
    findall(I, (symptom(I, S), member(S, Symptoms)), PossibleIllnesses),
    list_to_set(PossibleIllnesses, UniqueIllnesses),
    member(Illness, UniqueIllnesses).
    

test_diagnosis(Symptoms) :-
    % Symptoms = [sneezing, runny_nose, sore_throat],
    diagnose(Illness, Symptoms),
    write('Based on the given symptoms, the likely illness is: '),
    writeln(Illness).


% Example:
%test_diagnosis([sore_throat, fever, swollen_lymph_nodes, rash]).

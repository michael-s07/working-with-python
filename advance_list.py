names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records=list(zip(insurance_costs, names))
print(medical_records)

num_medical_records=len(medical_records)
print("There are "+str(num_medical_records)+" medical records. ")

first_medical_record=medical_records[:1]
print("Here is the first medical record: "+str(first_medical_record))

sort_medical_record=sorted(medical_records)
print("Here are the medicsl records sorted by the insurance cost: "+str(sort_medical_record))

cheapest_three=sort_medical_record[:3]
print("Here are the three cheapest insurance costs in our medical records: "+str(cheapest_three))

priciest_three=sort_medical_record[-3:]
print("Here are the three most expensive insurance costs in our medical records: "+str(priciest_three))

occurrences_paul=names.count("Paul")
print("There are "+str(occurrences_paul)+" individuals with the name Paul in our medical records.")



from fhirclient import client
import fhirclient.models.patient as p
parametros = {
    'app_id': 'pepito',
    'api_base': 'http://nprogram.azurewebsites.net/'
}
smart = client.FHIRClient(settings=parametros)

patient = p.Patient.read('10', smart.server)
print(patient.birthDate.isostring)
print(patient.gender)
print(smart.human_name(patient.name[0]))
print(patient.address)

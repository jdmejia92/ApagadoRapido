# Apagado Rápido

Este programa permite apagar el equipo de forma rápida, cerrando todos los programas, antes de proceder a con el apagado.

---

## Instalación

Para poder hacer uso del programa, deben seguir los siguientes pasos:

1. Escoger la carpeta donde deseas clonar el repositorio.
2. Proceder a clonar el repositorio dentro de dicha carpeta con el siguiente comando:

```powershell
Git Clone - dirección del repositorio
```

3. Una vez en la carpeta, solo debes ejecutarlo desde la consola.

```powershell
python ApagadoRapido.py
```

---

## Ejecutable

Una vez que haya procedido con los pasos anteriores, y solo si lo desea, puede crear un ejecutable del programa utilizando PyInstaller. Para ello debe seguir los siguientes pasos:

1.  Debe proceder a crear un ambiente virtual en la carpeta donde realizo la clonación del repositorio:

```powershell
python -m venv NombreDelAmbienteVirtual
```

2. Una vez creado el ambiente virtual hay que proceder a activarlos, para el caso de windows es:

```powershell
NombreDelAmbienteVirtual/scripts/activate
```

3. Una vez dentro del ambiente virtual solo debe proceder a copiar el contenido de **requirements.txt**, con el comando **pip**.

```powershell
pip freeze requirements.txt
```
4. Una vez finalizada la instalación de PyInstaller, solo debe ejecutar el último comando:

```powershell
pyinstaller --onefile ApagadoRapido.py
```

5. Encontrarás el ejecutable dentro de la carpeta **dist** generada por pyinstaller, al hacer doble clic en ese ejecutable podrás utilizar el programa de forma inmediata.

---
---
Espero les sea útil este programa para momentos de emergencia, fue creado pensando en problemas eléctricos y la necesidad de apagar lo antes posible el equipo, ya que el UPS que tenía no duraba mucho tiempo.
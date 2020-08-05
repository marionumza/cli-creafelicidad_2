# PROYECTO - CREAFELICIDAD
## REQUERIMIENTOS COMERCIALES
### REQU. DEL SISTEMA [2/2]
* Se deben poder crear multiples compañias en la misma base de datos
* Se deben poder crear multiples sucursales o unidades operativas dentro de la misma compañia
### REQU. DE MODULOS DEL SISTEMA [RESUELTO 8/8]
* Compras (Base)
* Ventas (Base)
* Contabilidad (Base)
* Inventario (Base)
* Terminal de Punto de Venta o POS
* Knowledge
* RRHH
* Whatsapp

### REQU. ESTRUCTURA EMPRESARIAL DEL SISTEMA [RESUELTO 3/3]
* La estructura de las compañias deben tener el siguiente sistema de estructura [OK]
 * Holding
   * Empresa 1
     * UO 1 (POS)
     * UO 2 (POS)
   * Empresa 2
     * UO 1 (POS)
     * UO 2 (POS)
     * UO 3 (POS)
     * UO 4 (VENTAS)
* Las compañias hijas deben tener configurada la contabilidad anglosajona [OK]
* Debe ser escalable para desactivar o crear nuevas compañias o unidades operativas [OK]
### REQU. PUNTO DE VENTA (POS) [RESUELTO 6/6]
* Se debe poder crear combos dinamicos con los productos [OK]
  * Las conbinaciones de combos se deben poder realizar desde el POS de forma dinámica
  * Debe descontar bien el stock
* Se deben poder crear promociones dinámicas que se disparen con ciertas reglas [OK]
  * Reglas pueden ser horarias (Happy Hour)
  * Reglas por fechas (Dia del amigo, dia del trabajador, apertura nuevo local, etc)
* Se debe poder emitir ticket/factura desde la comandera [OK]
* Se debe poder imprimir el pedido antes del pago [OK]
* Se deben poder habrir multiples sesiones sincronizadas entre si [OK]
* Se deben poder imprimir comandas [OK]
### REQU. COMPRAS
### REQU. VENTAS
### REQU. CONTABILIDAD



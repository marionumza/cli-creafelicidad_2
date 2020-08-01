# PROYECTO - CREAFELICIDAD
## REQUERIMIENTOS COMERCIALES
### REQU. ESTRUCTURA EMPRESARIAL DEL SISTEMA [RESUELTO]
* La estructura de las compañias deben tener el siguiente sistema de estructura [OK]
 * Holding [OK]
   * Empresa 1
     * UO 1 (POS)
     * UO 2 (POS)
   * Empresa 2
     * UO 1 (POS)
     * UO 2 (POS)
     * UO 3 (POS)
     * UO 4 (VENTAS)
* Las compañias hijas deben tener configurada la contabilidad anglosajona [OK]
* Debe ser escalable para desactivar o crear nuevas compañias o unidades operativas
### REQU. PUNTO DE VENTA (POS)
* Se debe poder crear combos dinamicos con los productos
  * Las conbinaciones de combos se deben poder realizar desde el POS de forma dinámica
  * Debe descontar bien el stock
* Se deben poder crear promociones dinámicas que se disparen con ciertas reglas
  * Reglas pueden ser horarias (Happy Hour)
  * Reglas por fechas (Dia del amigo, dia del trabajador, apertura nuevo local, etc)
* Se debe poder emitir ticket/factura desde la comandera
* Se debe poder imprimir el pedido antes del pago
* Se deben poder habrir multiples sesiones sincronizadas entre si
* Se deben poder imprimir comandas


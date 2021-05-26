
CREATE PROCEDURE [iEnergyDWH].[sp_del_pipeline_audit_log] @start_dt nvarchar(300),
     @end_dt nvarchar(300)
AS
 
BEGIN TRY  
 
   BEGIN TRANSACTION -- BEGIN TRAN statement will increment transaction count from 0 to 1
   DELETE FROM [iEnergyDWH].[pipeline_audit_log_t] 
   where format(created_dt,'yyyy-MM-dd') >= format(convert(date,@start_dt),'yyyy-MM-dd')
   and format(created_dt,'yyyy-MM-dd') <= format(convert(date,@end_dt),'yyyy-MM-dd');    
      
   COMMIT TRANSACTION -- COMMIT will decrement transaction count from 1 to 0 if dml worked
 
END TRY  
BEGIN CATCH  
   IF @@TRANCOUNT > 0  
      ROLLBACK  
 
   -- Return error information. 
   DECLARE @ErrorMessage nvarchar(4000),  @ErrorSeverity int;  
   SELECT @ErrorMessage = ERROR_MESSAGE(),@ErrorSeverity = ERROR_SEVERITY();  
   RAISERROR(@ErrorMessage, @ErrorSeverity, 1);  
END CATCH;  
 
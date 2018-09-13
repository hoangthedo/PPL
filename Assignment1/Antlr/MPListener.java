// Generated from MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MPParser}.
 */
public interface MPListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MPParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MPParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#manydec}.
	 * @param ctx the parse tree
	 */
	void enterManydec(MPParser.ManydecContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#manydec}.
	 * @param ctx the parse tree
	 */
	void exitManydec(MPParser.ManydecContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#onedec}.
	 * @param ctx the parse tree
	 */
	void enterOnedec(MPParser.OnedecContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#onedec}.
	 * @param ctx the parse tree
	 */
	void exitOnedec(MPParser.OnedecContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#vardec}.
	 * @param ctx the parse tree
	 */
	void enterVardec(MPParser.VardecContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#vardec}.
	 * @param ctx the parse tree
	 */
	void exitVardec(MPParser.VardecContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#varlist}.
	 * @param ctx the parse tree
	 */
	void enterVarlist(MPParser.VarlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#varlist}.
	 * @param ctx the parse tree
	 */
	void exitVarlist(MPParser.VarlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#vartypelist}.
	 * @param ctx the parse tree
	 */
	void enterVartypelist(MPParser.VartypelistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#vartypelist}.
	 * @param ctx the parse tree
	 */
	void exitVartypelist(MPParser.VartypelistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#vartype}.
	 * @param ctx the parse tree
	 */
	void enterVartype(MPParser.VartypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#vartype}.
	 * @param ctx the parse tree
	 */
	void exitVartype(MPParser.VartypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#paramarr}.
	 * @param ctx the parse tree
	 */
	void enterParamarr(MPParser.ParamarrContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#paramarr}.
	 * @param ctx the parse tree
	 */
	void exitParamarr(MPParser.ParamarrContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#vartypebasic}.
	 * @param ctx the parse tree
	 */
	void enterVartypebasic(MPParser.VartypebasicContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#vartypebasic}.
	 * @param ctx the parse tree
	 */
	void exitVartypebasic(MPParser.VartypebasicContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#funcdec}.
	 * @param ctx the parse tree
	 */
	void enterFuncdec(MPParser.FuncdecContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#funcdec}.
	 * @param ctx the parse tree
	 */
	void exitFuncdec(MPParser.FuncdecContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#paramlist}.
	 * @param ctx the parse tree
	 */
	void enterParamlist(MPParser.ParamlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#paramlist}.
	 * @param ctx the parse tree
	 */
	void exitParamlist(MPParser.ParamlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#paramsingle}.
	 * @param ctx the parse tree
	 */
	void enterParamsingle(MPParser.ParamsingleContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#paramsingle}.
	 * @param ctx the parse tree
	 */
	void exitParamsingle(MPParser.ParamsingleContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#returntype}.
	 * @param ctx the parse tree
	 */
	void enterReturntype(MPParser.ReturntypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#returntype}.
	 * @param ctx the parse tree
	 */
	void exitReturntype(MPParser.ReturntypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(MPParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(MPParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#assignstmt}.
	 * @param ctx the parse tree
	 */
	void enterAssignstmt(MPParser.AssignstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#assignstmt}.
	 * @param ctx the parse tree
	 */
	void exitAssignstmt(MPParser.AssignstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#assignlist}.
	 * @param ctx the parse tree
	 */
	void enterAssignlist(MPParser.AssignlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#assignlist}.
	 * @param ctx the parse tree
	 */
	void exitAssignlist(MPParser.AssignlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#arrayvar}.
	 * @param ctx the parse tree
	 */
	void enterArrayvar(MPParser.ArrayvarContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#arrayvar}.
	 * @param ctx the parse tree
	 */
	void exitArrayvar(MPParser.ArrayvarContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#funcstmt}.
	 * @param ctx the parse tree
	 */
	void enterFuncstmt(MPParser.FuncstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#funcstmt}.
	 * @param ctx the parse tree
	 */
	void exitFuncstmt(MPParser.FuncstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#ifstmt}.
	 * @param ctx the parse tree
	 */
	void enterIfstmt(MPParser.IfstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#ifstmt}.
	 * @param ctx the parse tree
	 */
	void exitIfstmt(MPParser.IfstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#ifexp}.
	 * @param ctx the parse tree
	 */
	void enterIfexp(MPParser.IfexpContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#ifexp}.
	 * @param ctx the parse tree
	 */
	void exitIfexp(MPParser.IfexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#ifbody}.
	 * @param ctx the parse tree
	 */
	void enterIfbody(MPParser.IfbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#ifbody}.
	 * @param ctx the parse tree
	 */
	void exitIfbody(MPParser.IfbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#whilestmt}.
	 * @param ctx the parse tree
	 */
	void enterWhilestmt(MPParser.WhilestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#whilestmt}.
	 * @param ctx the parse tree
	 */
	void exitWhilestmt(MPParser.WhilestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#whileexp}.
	 * @param ctx the parse tree
	 */
	void enterWhileexp(MPParser.WhileexpContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#whileexp}.
	 * @param ctx the parse tree
	 */
	void exitWhileexp(MPParser.WhileexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#whilebody}.
	 * @param ctx the parse tree
	 */
	void enterWhilebody(MPParser.WhilebodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#whilebody}.
	 * @param ctx the parse tree
	 */
	void exitWhilebody(MPParser.WhilebodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#forstmt}.
	 * @param ctx the parse tree
	 */
	void enterForstmt(MPParser.ForstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#forstmt}.
	 * @param ctx the parse tree
	 */
	void exitForstmt(MPParser.ForstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#forbody}.
	 * @param ctx the parse tree
	 */
	void enterForbody(MPParser.ForbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#forbody}.
	 * @param ctx the parse tree
	 */
	void exitForbody(MPParser.ForbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#breakstmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakstmt(MPParser.BreakstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#breakstmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakstmt(MPParser.BreakstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#continuestmt}.
	 * @param ctx the parse tree
	 */
	void enterContinuestmt(MPParser.ContinuestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#continuestmt}.
	 * @param ctx the parse tree
	 */
	void exitContinuestmt(MPParser.ContinuestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#compoundstmt}.
	 * @param ctx the parse tree
	 */
	void enterCompoundstmt(MPParser.CompoundstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#compoundstmt}.
	 * @param ctx the parse tree
	 */
	void exitCompoundstmt(MPParser.CompoundstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#returnstmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnstmt(MPParser.ReturnstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#returnstmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnstmt(MPParser.ReturnstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#returnbody}.
	 * @param ctx the parse tree
	 */
	void enterReturnbody(MPParser.ReturnbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#returnbody}.
	 * @param ctx the parse tree
	 */
	void exitReturnbody(MPParser.ReturnbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#withstmt}.
	 * @param ctx the parse tree
	 */
	void enterWithstmt(MPParser.WithstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#withstmt}.
	 * @param ctx the parse tree
	 */
	void exitWithstmt(MPParser.WithstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#funcall}.
	 * @param ctx the parse tree
	 */
	void enterFuncall(MPParser.FuncallContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#funcall}.
	 * @param ctx the parse tree
	 */
	void exitFuncall(MPParser.FuncallContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#calllist}.
	 * @param ctx the parse tree
	 */
	void enterCalllist(MPParser.CalllistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#calllist}.
	 * @param ctx the parse tree
	 */
	void exitCalllist(MPParser.CalllistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#procdec}.
	 * @param ctx the parse tree
	 */
	void enterProcdec(MPParser.ProcdecContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#procdec}.
	 * @param ctx the parse tree
	 */
	void exitProcdec(MPParser.ProcdecContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#procmain}.
	 * @param ctx the parse tree
	 */
	void enterProcmain(MPParser.ProcmainContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#procmain}.
	 * @param ctx the parse tree
	 */
	void exitProcmain(MPParser.ProcmainContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#procbasic}.
	 * @param ctx the parse tree
	 */
	void enterProcbasic(MPParser.ProcbasicContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#procbasic}.
	 * @param ctx the parse tree
	 */
	void exitProcbasic(MPParser.ProcbasicContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#expstmt}.
	 * @param ctx the parse tree
	 */
	void enterExpstmt(MPParser.ExpstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#expstmt}.
	 * @param ctx the parse tree
	 */
	void exitExpstmt(MPParser.ExpstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(MPParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(MPParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MPParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MPParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#exp1}.
	 * @param ctx the parse tree
	 */
	void enterExp1(MPParser.Exp1Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#exp1}.
	 * @param ctx the parse tree
	 */
	void exitExp1(MPParser.Exp1Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#exp2}.
	 * @param ctx the parse tree
	 */
	void enterExp2(MPParser.Exp2Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#exp2}.
	 * @param ctx the parse tree
	 */
	void exitExp2(MPParser.Exp2Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#exp3}.
	 * @param ctx the parse tree
	 */
	void enterExp3(MPParser.Exp3Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#exp3}.
	 * @param ctx the parse tree
	 */
	void exitExp3(MPParser.Exp3Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#exp4}.
	 * @param ctx the parse tree
	 */
	void enterExp4(MPParser.Exp4Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#exp4}.
	 * @param ctx the parse tree
	 */
	void exitExp4(MPParser.Exp4Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#exp5}.
	 * @param ctx the parse tree
	 */
	void enterExp5(MPParser.Exp5Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#exp5}.
	 * @param ctx the parse tree
	 */
	void exitExp5(MPParser.Exp5Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#exp6}.
	 * @param ctx the parse tree
	 */
	void enterExp6(MPParser.Exp6Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#exp6}.
	 * @param ctx the parse tree
	 */
	void exitExp6(MPParser.Exp6Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#literals}.
	 * @param ctx the parse tree
	 */
	void enterLiterals(MPParser.LiteralsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#literals}.
	 * @param ctx the parse tree
	 */
	void exitLiterals(MPParser.LiteralsContext ctx);
}
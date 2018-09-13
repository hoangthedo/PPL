// Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MPParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MPVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MPParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#vardec}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVardec(MPParser.VardecContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#var1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar1(MPParser.Var1Context ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#vartype}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVartype(MPParser.VartypeContext ctx);
}
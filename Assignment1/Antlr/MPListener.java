// Generated from MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MPParser}.
 */
public interface MPListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MPParser#comment}.
	 * @param ctx the parse tree
	 */
	void enterComment(MPParser.CommentContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#comment}.
	 * @param ctx the parse tree
	 */
	void exitComment(MPParser.CommentContext ctx);
}
/**
 * @module ol/renderer/canvas/Layer
 */
import {getBottomLeft, getBottomRight, getTopLeft, getTopRight} from '../../extent.js';
import {TRUE} from '../../functions.js';
import RenderEvent from '../../render/Event.js';
import RenderEventType from '../../render/EventType.js';
import {rotateAtOffset} from '../../render/canvas.js';
import CanvasImmediateRenderer from '../../render/canvas/Immediate.js';
import LayerRenderer from '../Layer.js';
import {create as createTransform, apply as applyTransform, compose as composeTransform} from '../../transform.js';

var CanvasLayerRenderer = (function (LayerRenderer) {
  function CanvasLayerRenderer(layer) {

    LayerRenderer.call(this, layer);

    /**
     * @protected
     * @type {number}
     */
    this.renderedResolution;

    /**
     * @private
     * @type {module:ol/transform~Transform}
     */
    this.transform_ = createTransform();

  }

  if ( LayerRenderer ) CanvasLayerRenderer.__proto__ = LayerRenderer;
  CanvasLayerRenderer.prototype = Object.create( LayerRenderer && LayerRenderer.prototype );
  CanvasLayerRenderer.prototype.constructor = CanvasLayerRenderer;

  /**
   * @param {CanvasRenderingContext2D} context Context.
   * @param {module:ol/PluggableMap~FrameState} frameState Frame state.
   * @param {module:ol/extent~Extent} extent Clip extent.
   * @protected
   */
  CanvasLayerRenderer.prototype.clip = function clip (context, frameState, extent) {
    var pixelRatio = frameState.pixelRatio;
    var width = frameState.size[0] * pixelRatio;
    var height = frameState.size[1] * pixelRatio;
    var rotation = frameState.viewState.rotation;
    var topLeft = getTopLeft(/** @type {module:ol/extent~Extent} */ (extent));
    var topRight = getTopRight(/** @type {module:ol/extent~Extent} */ (extent));
    var bottomRight = getBottomRight(/** @type {module:ol/extent~Extent} */ (extent));
    var bottomLeft = getBottomLeft(/** @type {module:ol/extent~Extent} */ (extent));

    applyTransform(frameState.coordinateToPixelTransform, topLeft);
    applyTransform(frameState.coordinateToPixelTransform, topRight);
    applyTransform(frameState.coordinateToPixelTransform, bottomRight);
    applyTransform(frameState.coordinateToPixelTransform, bottomLeft);

    context.save();
    rotateAtOffset(context, -rotation, width / 2, height / 2);
    context.beginPath();
    context.moveTo(topLeft[0] * pixelRatio, topLeft[1] * pixelRatio);
    context.lineTo(topRight[0] * pixelRatio, topRight[1] * pixelRatio);
    context.lineTo(bottomRight[0] * pixelRatio, bottomRight[1] * pixelRatio);
    context.lineTo(bottomLeft[0] * pixelRatio, bottomLeft[1] * pixelRatio);
    context.clip();
    rotateAtOffset(context, rotation, width / 2, height / 2);
  };

  /**
   * @param {module:ol/render/EventType} type Event type.
   * @param {CanvasRenderingContext2D} context Context.
   * @param {module:ol/PluggableMap~FrameState} frameState Frame state.
   * @param {module:ol/transform~Transform=} opt_transform Transform.
   * @private
   */
  CanvasLayerRenderer.prototype.dispatchComposeEvent_ = function dispatchComposeEvent_ (type, context, frameState, opt_transform) {
    var layer = this.getLayer();
    if (layer.hasListener(type)) {
      var width = frameState.size[0] * frameState.pixelRatio;
      var height = frameState.size[1] * frameState.pixelRatio;
      var rotation = frameState.viewState.rotation;
      rotateAtOffset(context, -rotation, width / 2, height / 2);
      var transform = opt_transform !== undefined ?
        opt_transform : this.getTransform(frameState, 0);
      var render = new CanvasImmediateRenderer(
        context, frameState.pixelRatio, frameState.extent, transform,
        frameState.viewState.rotation);
      var composeEvent = new RenderEvent(type, render, frameState,
        context, null);
      layer.dispatchEvent(composeEvent);
      rotateAtOffset(context, rotation, width / 2, height / 2);
    }
  };

  /**
   * @param {module:ol/coordinate~Coordinate} coordinate Coordinate.
   * @param {module:ol/PluggableMap~FrameState} frameState FrameState.
   * @param {number} hitTolerance Hit tolerance in pixels.
   * @param {function(this: S, module:ol/layer/Layer, (Uint8ClampedArray|Uint8Array)): T} callback Layer
   *     callback.
   * @param {S} thisArg Value to use as `this` when executing `callback`.
   * @return {T|undefined} Callback result.
   * @template S,T,U
   */
  CanvasLayerRenderer.prototype.forEachLayerAtCoordinate = function forEachLayerAtCoordinate (coordinate, frameState, hitTolerance, callback, thisArg) {
    var hasFeature = this.forEachFeatureAtCoordinate(coordinate, frameState, hitTolerance, TRUE, this);

    if (hasFeature) {
      return callback.call(thisArg, this.getLayer(), null);
    } else {
      return undefined;
    }
  };

  /**
   * @param {CanvasRenderingContext2D} context Context.
   * @param {module:ol/PluggableMap~FrameState} frameState Frame state.
   * @param {module:ol/layer/Layer~State} layerState Layer state.
   * @param {module:ol/transform~Transform=} opt_transform Transform.
   * @protected
   */
  CanvasLayerRenderer.prototype.postCompose = function postCompose (context, frameState, layerState, opt_transform) {
    this.dispatchComposeEvent_(RenderEventType.POSTCOMPOSE, context, frameState, opt_transform);
  };

  /**
   * @param {CanvasRenderingContext2D} context Context.
   * @param {module:ol/PluggableMap~FrameState} frameState Frame state.
   * @param {module:ol/transform~Transform=} opt_transform Transform.
   * @protected
   */
  CanvasLayerRenderer.prototype.preCompose = function preCompose (context, frameState, opt_transform) {
    this.dispatchComposeEvent_(RenderEventType.PRECOMPOSE, context, frameState, opt_transform);
  };

  /**
   * @param {CanvasRenderingContext2D} context Context.
   * @param {module:ol/PluggableMap~FrameState} frameState Frame state.
   * @param {module:ol/transform~Transform=} opt_transform Transform.
   * @protected
   */
  CanvasLayerRenderer.prototype.dispatchRenderEvent = function dispatchRenderEvent (context, frameState, opt_transform) {
    this.dispatchComposeEvent_(RenderEventType.RENDER, context, frameState, opt_transform);
  };

  /**
   * @param {module:ol/PluggableMap~FrameState} frameState Frame state.
   * @param {number} offsetX Offset on the x-axis in view coordinates.
   * @protected
   * @return {!module:ol/transform~Transform} Transform.
   */
  CanvasLayerRenderer.prototype.getTransform = function getTransform (frameState, offsetX) {
    var viewState = frameState.viewState;
    var pixelRatio = frameState.pixelRatio;
    var dx1 = pixelRatio * frameState.size[0] / 2;
    var dy1 = pixelRatio * frameState.size[1] / 2;
    var sx = pixelRatio / viewState.resolution;
    var sy = -sx;
    var angle = -viewState.rotation;
    var dx2 = -viewState.center[0] + offsetX;
    var dy2 = -viewState.center[1];
    return composeTransform(this.transform_, dx1, dy1, sx, sy, angle, dx2, dy2);
  };

  /**
   * @abstract
   * @param {module:ol/PluggableMap~FrameState} frameState Frame state.
   * @param {module:ol/layer/Layer~State} layerState Layer state.
   * @param {CanvasRenderingContext2D} context Context.
   */
  CanvasLayerRenderer.prototype.composeFrame = function composeFrame (frameState, layerState, context) {};

  /**
   * @abstract
   * @param {module:ol/PluggableMap~FrameState} frameState Frame state.
   * @param {module:ol/layer/Layer~State} layerState Layer state.
   * @return {boolean} whether composeFrame should be called.
   */
  CanvasLayerRenderer.prototype.prepareFrame = function prepareFrame (frameState, layerState) {};

  return CanvasLayerRenderer;
}(LayerRenderer));

export default CanvasLayerRenderer;

//# sourceMappingURL=Layer.js.map